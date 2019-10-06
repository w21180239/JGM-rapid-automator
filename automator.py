from target import TargetType
from cv import UIMatcher
import uiautomator2 as u2
from datetime import datetime,timedelta
import time
import cv2
import inspect


class Automator:
    def __init__(self, device: str, targets: dict,mode:str):
        # device: 如果是 USB 连接，则为 adb devices 的返回结果；如果是模拟器，则为模拟器的控制 URL 。
        self.mode = '拉货'
        self.d = u2.connect(device)
        self.targets = targets
        self.positions = {
            1: (294, 1184),
            2: (551, 1061),
            3: (807, 961),
            4: (275, 935),
            5: (535, 810),
            6: (799, 687),
            7: (304, 681),
            8: (541, 568),
            9: (787, 447),
            '福气':(217,831),
            '多福':(545,846),
            '满福':(878,829),
            '相册':(533, 1447)
        }
        self.mode = mode

    def start(self):
        sleep_time = 3      #两次检测之间的间隔
        no_train_counter = 0        #连续没有检测到火车的次数
        train_image = cv2.imread('Train.jpg')
        good_counter = 0
        restart_counter = 0
        while True:
            if self.mode !='拉货':
                self.d.click(*self.positions[self.mode])
            else:
                # 判断是否出现货物。
                Screen = self.d.screenshot(format="opencv")
                self.d.click(550, 1650)

                # 滑动屏幕，收割金币。
                self._swipe()
                if UIMatcher.Detect_signal_object(Screen, train_image):
                    print('火车来了！')
                    no_train_counter = 0
                    success_counter = 0
                    time.sleep(1)       #确保火车停了下来
                    screen = self.d.screenshot(format="opencv")
                    for target in TargetType:
                        if success_counter > 2:
                            print('成功找到3个货物，提前结束！')
                            break
                        if self._match_target(target,screen):
                            print(f'寻找{target.name}-------------------成功')
                            success_counter += 1
                            good_counter += 1
                        else:
                            print(f'寻找{target.name}-------------------失败')
                            # if target in self.ban_list:
                    print(f'重启游戏...')
                    restart_counter += 1
                    self.d.app_stop("com.tencent.jgm")
                    self.d.app_start("com.tencent.jgm")
                    time.sleep(20)


                else:
                    no_train_counter+=1
                    if no_train_counter>=20:
                        print(f'连续{no_train_counter*sleep_time}s没有检测到火车,结束脚本！')
                        print(f'脚本运行期间一共\n拉取了--------------------{good_counter}次货物\n重启了--------------------{restart_counter}次')
                        return
                time.sleep(sleep_time)



    def _swipe(self):
        # 滑动屏幕，收割金币。
        for i in range(3):
            # 横向滑动，共 3 次。
            sx, sy = self._get_position(i * 3 + 1)
            ex, ey = self._get_position(i * 3 + 3)
            self.d.swipe(sx, sy, ex, ey)

    def _get_position(self,key):
        # 获取指定建筑的屏幕位置。
        return self.positions.get(key)

    def _get_target_position(self, target: TargetType):
        # 获取货物要移动到的屏幕位置。
        return self._get_position(self.targets.get(target))

    def _match_target(self, target: TargetType,screen):
        # 探测货物，并搬运货物。

        result = UIMatcher.match(screen, target)
        if result is not None:
            sx, sy = result
            # 获取货物目的地的屏幕位置。
            ex, ey = self._get_target_position(target)

            # 搬运货物。
            for j in range(2):
                self.d.swipe(sx, sy, ex, ey)
            return True
        return False


