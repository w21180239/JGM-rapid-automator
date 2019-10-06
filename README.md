# 高效家国梦自动收割脚本

> 这是基于 OpenCV 模板匹配的《家国梦》游戏自动化脚本。
> 建议与[家国梦最佳建筑摆放计算](https://github.com/SQRPI/JiaGuoMeng)一起使用

## 安装与运行

```bash
# 安装依赖
python -m pip install uiautomator2 opencv-python

# adb 连接
# 使用 MuMu 模拟器，确保屏幕大小为 1920（长） * 1080（宽）
adb connect 127.0.0.1:7555

# 获取 device 名称,并填写至 main.py,如果用的是MuMU（推荐）就忽略这一步
adb devices

# 在已完成 adb 连接后，在手机安装 ATX 应用
python -m uiautomator2 init

# 打开 ATX ，点击“启动 UIAutomator”选项，确保 UIAutomator 是运行的。

# 进入游戏页面，启动自动脚本。
python main.py
```
## 自定义
请在target.py和main.py中根据自己的实际情况修改货物种类和建筑物位置，如需添加新的货物类型请再1920*1080分辨率下的MuMu中截图并添加。

##Weditor

我们可以使用 Weditor 工具，获取屏幕坐标，以及在线编写自动化脚本。

```bash
# 安装依赖
python -m pip install --pre weditor

# 启动 Weditor
python -m weditor
```

## 2019/10/6
- 新增3种脚本模式：福气，多福，相册，分别用来自动开启福气红包，多福红包与相册，但是考虑到点击速度，未添加次数限制，请点完红包后手动重启
- 更新README.md
- 考虑到供货党的实际需求，火车来的时候只拉取金色货物，由于很少在一趟火车中出现全是金色货物的情况，所以拉取完货物之后必定重启。请根据自身金色建筑的拥有和摆放情况修改target.py和main.py
- 新增WEditor的相关使用说明，可用于查看坐标，方便修改代码