import pyautogui, keyboard, mouse
from time import sleep
banner1="""
   _  ____________     ___         __             ___      __            
  | |/ /_  __/ __ \   /   | __  __/ /_____  _____/ (_)____/ /_____  _____
  |   / / / / /_/ /  / /| |/ / / / __/ __ \/ ___/ / / ___/ //_/ _ \/ ___/
 /   | / / / _, _/  / ___ / /_/ / /_/ /_/ / /__/ / / /__/ ,< /  __/ /    
/_/|_|/_/ /_/ |_|  /_/  |_\__,_/\__/\____/\___/_/_/\___/_/|_|\___/_/     
                                                                         """
banner="""BY RAV3NPHO3NIX\n- 'q' to quit\n- 'r' to restart the program"""
def loop(x,y):
    while True:
        mouse.move(x,y)
        mouse.click()
        if keyboard.is_pressed('q'):break
        elif keyboard.is_pressed('r'):click()
        elif keyboard.is_pressed(stopButton):pause(x,y)
        sleep(delay/1000)
def click():
    print("Click where you want to autoclick")
    mouse.wait(button='left')
    x,y=pyautogui.position()
    print(f"Position: {x}, {y}")
    pause(x,y)
def pause(x,y):
    key=keyboard.read_key()
    if key==('q'):exit()
    elif key==('r'):click()
    elif key==(startButton):loop(x,y)
    else: pause(x,y)
def main():
    print(f"{banner1}\n{banner}")
    global startButton
    startButton=input("Which button you want to choose to start the autoclick ?: ('s' by default) ")
    if startButton=='': startButton='s'
    global stopButton
    stopButton=input("Wich button you want to choose to pause the autoclick ?: ('p' by default) ")
    if stopButton=='': stopButton='p'
    global delay
    delay=input("What are the delay between tho clics in ms ?: (1 by default)")
    if delay=='': delay=1
    click()
main()