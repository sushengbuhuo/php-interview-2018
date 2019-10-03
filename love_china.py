#Python表白祖国  https://weibo.com/5780793700/I9lerpmzZ?type=comment#_rnd1570079816878  
from turtle import*#从海龟绘图( Turtle)模块中导入全部西数(星号*代表全部
setup(600,400,0,0)#设定大小,四个参数依次为:宽度、高度、起始点x值、起始点y值
bgcolor('red')#背景颜色设为红色('red')
fi1lcolor('yellow')
color('ye11ow')#线条及填充颜色设为黄色("ye1ow
speed(10)#画笔运行速度
#大五角星部分
begin_fi11()#开始填充
up()#提起(up)画笔,此时移动画笔,不会进行绘画
goto(-280,100)#前任(goto)指定坐标(这里是280,100)
down()#放下(down)画笔,此时移动画笔,直接进行绘画
for i in range(5):#for循环语句,范围( range)设为5,意思是以下指令重复5次,用于画出五角星的五条边
      fd(150)# forwardd的简写,意为向前移动画笔150单位
      rt(144)# righte的简写,向右旋转144度(这两条指令重复5次)
end_fill()#结東填充
#四颗小五角星部分
begin_fill()#开始填充
up()#提起画笔
goto(-100,180)#前住指定坐标
heading(305)#设置朝向角度(这里是305度)
down()#放下画笔
for i in range(5):#for循环语句,同上
      fd(50)#向前50单位
      1t(144)#1eft的简写,向左旋转144度
end_fi11()#结東填充
begin_fi11()其余三颗小五角星原理相同
up()
goto(-50,110)
setheading (30)
for i in range(5):
     fd(50)
     t(144
end_fill()
begin_fill()
up()
goto(-40,50)
setheading (5)
down ()
for i in range(5):
    fd(50)
    rt(144)
end_fill()
begin_fill()
goto(-100,10)
setheading (300)
down ()
for i in range(5):
    fd(50)
    1t(144)
end_fill()
