from machine import Pin, I2C
import _thread
from utime import sleep
from ssd1306 import SSD1306_I2C

i2c = I2C(0, scl = Pin(13), sda = Pin(12), freq = 400000) # Set the SCL and SDA pins for I2C communication, SCL on GPIO13 and SDA on GPIO12
display = SSD1306_I2C(128, 64, i2c)

# Below is 83 key musical note
A1,b1,B1,C1,d1,D1,e1,E1,F1,g1,G1,a1,A2,b2,B2,C2,d2,D2,e2,E2,F2,g2,G2,a2,A3,b3,B3,C3,d3,D3,e3,E3,F3,g3,G3,a3,A4,b4,B4,C4,d4,D4,e4,E4,F4,g4,G4,a4,A5,b5,B5,C5,d5,D5,e5,E5,F5,g5,G5,a5,A6,b6,B6,C6,d6,D6,e6,E6,F6,g6,G6,a6,A7,b7,B7,C7,d7,D7,e7,E7,F7,g7,G7,a7=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83


# Notes arary for Fur Elise
fur = [E4,e4,E4,e4,E4,B4,D4,C4,A4,E2,A2,C3,E3,A3,B3,E2,a2,E3,a3,B3,C4,E2,A2,E4,e4,E4,e4,E4,B4,D4,C4,A4,E2,A2,C3,E3,A3,B3,E2,a2,E3,C4,B3,A4,E2,A2,B3,C4,D4,E4,G2,C3,G3,F4,E4,D4,G2,B2,F3,E4,D4,C4,E2,A2,E3,D4,C4,B3,E3,E3,E4,E4,E5,e4,E4,e4,E4,e4,E4,e4,E4,e4,E4,B4,D4,C4,A4,E2,A2,C3,E3,A3,B3,E2,a2,E3,a3,B3,C4,E2,A2,E4,e4,E4,e4,E4,B4,D4,C4,A4,E2,A2,C3,E3,A3,B3,E2,a2,E3,C4,B3,A4,E2,A2,B3,C4,D4,E4,G2,C3,G3,F4,E4,D4,G2,B2,F3,E4,D4,C4,E2,A2,E3,D4,C4,B3,E3,E3,E4,E4,E5,e4,E4,e4,E4,e4]
# Delay array for delay between each notes
furdel = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

# Notes arary for Harry Potter theme
hp= [B3,E4,G4,g4,E4,B4,A4,g4,E4,G4,g4,e4,E4,B3,B3,E4,G4,g4,E4,B4,D5,d5,C5,a4,C5,B4,b4,b3,G4,E4,G4,B4,G4,B4,G4,C5,B4,b4,g4,G4,B4,b4,b3,C4,B4,G4,B4,G4,B4,G4,D5,d5,C5,a4,C5,B4,b4,b3,G3,E3]
# Delay array for delay between each notes
hpdel = [2,3,1,2,4,2,6,6,3,1,2,4,2,10,2,3,1,2,4,2,4,2,4,2,3,1,2,4,2,10,2,4,2,4,2,4,2,4,2,4,1,2,4,2,10,2,4,2,4,2,4,2,4,2,3,1,2,4,2,10]

# Notes for a random music
rand = [F3,C4,a4,F3,C4,G4,F3,C4,F4,F3,C4,F4,F3,e4,F4,d4,C4,F3,C4,a4,F3,C4,G4,F3,C4,F4,F3,C4,F4,F3,e4,F4,d4,C4,F3,C4,a4,F3,C4,G4,F3,C4,F4,F3,C4,F4,F3,e4,F4,d4,C4,e3,b3,F4,e3,b3,e4,e3,b3,d4,F3,b3,G4,a3,b3,C4,a3,G3]
# Delay array for delay between each notes
randdel = [1,1,1,1,1,1,1,1,1,1,1,1,1,0.5,0.5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0.5,0.5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0.5,0.5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0.5,0.5,1,1]

# Below is the function of the oscillator which can generate squarewave notes with a specific dutycycle
def Osc(key,dc):
    from machine import Pin, PWM
    a_ref = 55
    freq=int(a_ref*(2**(key/12)))
    ds = int((1/freq)*dc*10000000)
    pwm = PWM(Pin(16)) # Set up GPIO16 as speaker output
    pwm.freq(freq)
    pwm.duty_ns(ds)

# Function to play a melody using the above OSCILLATOR function. It takes a notes array with delay array and has dutycycle, transpose and playback speed options
def player(midi,delay,dc=50,tpose=0,spd=1):
    from utime import sleep
    midi_l=len(midi)
    if midi_l==len(delay):
        for i in range(midi_l):
            Osc(midi[i]+tpose,dc)
            sleep(delay[i]*spd)
        Osc(100,0)
        
# Below is the function to convert Portable Bit-Map Graphics (PBM) image files into Frame Buffers
def byteframes(location,img_x,img_y,totalframes,x=0,y=0):
    import framebuf as buff
    #x,y,totalframes=65,49,230
    img = []
    for n in range(1, totalframes + 1):
        display.fill(0)
        display.text("LOADING PBM %d"%((n/totalframes)*100)+"%",x,y)
        display.text("%d"%n,104,56)
        with open(location % n, 'rb') as f:
            f.readline()
            f.readline()
            f.readline()
            bitmap = bytearray(f.read())
        fbr = buff.FrameBuffer(bitmap,img_x, img_y, buff.MONO_HLSB)
        img.append(fbr)
        display.show()
        print("%s frame added"%n)
    f.close()
    display.fill(0)
    display.show()
    return img

# Function to play animation using the above BYTEFRAMES function. It takes frame-buffer array and gives feature to loop the animation, setting cursor of the animation and adjusting speed of animation
def animation(imgarray, loop=0, x=0, y=0, delay= 1/30):
    display.fill(0)
    def showmethod():
        for i in imgarray:
            display.blit(i, x, y)
            display.show()
            sleep(delay)
    if loop == 0: showmethod()
    else:
        while True: showmethod()
    display.fill(0)
    display.show()

str1 = 'cat2/image%s.pbm' # Location of PBM files
frames = byteframes(str1,61,49,25) # Conversion of PBM files

# Creating a different thread for raspberry pi pico to play audio with animation simultaneously
def mach_thread():
    while True:
        #player(hp,hpdel,60,-4,0.15) #harry potter theme
        #player(rand,randdel,20,-24,0.19) #random trap arp
        player(fur,furdel,20,-11,.2) #fur elise

_thread.start_new_thread(mach_thread,()) # Starting the thread which plays audio
animation(frames, 1, 0, 16, 0.05)  # Displaying animations on OLED display
