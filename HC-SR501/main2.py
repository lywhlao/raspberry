import RPi.GPIO as GPIO
import time
from datetime import datetime
from gpiozero import LED

# 全自动感应:人进入其感应范围则输出低电平，人离开感应范围则自动延时关闭低电平，输出高电平。

#红外传感器
GPIO_PIN = 18

#
GPIO_LED=5
def currentTime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

# 初始化
def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_PIN, GPIO.IN)
    GPIO.setup(GPIO_LED, GPIO.OUT)

def lightLed():
    led=LED(GPIO_LED)
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)


def humanIn(channel):
    print("detect {} human is in area,time{}==>".format(channel,currentTime()))
    lightLed()

# 感应器侦测函数
def detct():
    GPIO.add_event_detect(GPIO_PIN,GPIO.RA, callback=humanIn)

def initListener():
    GPIO.add_event_detect(GPIO_PIN,GPIO.RISING,bouncetime=200)

# 主程序入口
if __name__ == '__main__':
    init()
    # detct()
    initListener()
    try:
        while True:
            if GPIO.event_detected(GPIO_PIN):
                print("detect human is in area,time{}==>".format(currentTime()))
                lightLed()
            time.sleep(1)
            # if GPIO.input(GPIO_PIN) == True:
            #     lightLed()
            #     print("detect human is in area,time{}==>".format(currentTime()))
            #     time.sleep(1)
            # else:
            #     time.sleep(0.5)
            # 脚本运行完毕执行清理工作
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("stopped by User")
    GPIO.cleanup()  # 导入 GPIO库

