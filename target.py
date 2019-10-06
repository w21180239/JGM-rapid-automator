from enum import Enum
import cv2

class TargetType(Enum):
    # 货物枚举类型，请将没用到的建筑物对应的货物注释掉，提高程序运行效率
    
    # Chair = 'targets/Chair.jpg'
    # Vegetable = 'targets/Vegetable.jpg'
    # Bottle = 'targets/Bottle.jpg'
    # Wood = 'targets/Wood.jpg'
    # Food = 'targets/Food.jpg'
    # Box = 'targets/Box.jpg'
    # Book = 'targets/Book.jpg'
    # Bag = 'targets/Bag.jpg'
    # Coal = 'targets/Coal.jpg'
    # Grass = 'targets/Grass.jpg'
    # Sofa = 'targets/Sofa.jpg'
    Chicken = cv2.imread('targets/Chicken.jpg')
    # Cloth = 'targets/Cloth.jpg'
    # Cotton = 'targets/Cotton.jpg'
    # Plant = 'targets/Plant.jpg'
    # Stone = 'targets/Stone.jpg'
    Carpet = cv2.imread('targets/Carpet.jpg')
    # Computer = 'targets/Computer.jpg'
    # Dogfood = 'targets/Dogfood.jpg'
    Oil = cv2.imread('targets/Oil.jpg')
    # Quilt = 'targets/Quilt.jpg'
    # Screw = 'targets/Screw.jpg'
    # Shoes = 'targets/Shoes.jpg'
    Tool = cv2.imread('targets/Tool.jpg')
    Microphone = cv2.imread('targets/Microphone.jpg')
    # Armoire = 'targets/Armoire.jpg'

