import pyautogui
import time
import keyboard
import customtkinter as ctk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import os


print(pyautogui.size())
print(pyautogui.position())

nb_Stage_Finished = 0


# functions

def go_main_menu():
    time.sleep(5)
    if pyautogui.locateOnScreen('./img/home.png', region=(50, 310, 240, 200), confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/home.png', region=(50, 310, 240, 200), confidence=0.8))
        time.sleep(2)
    elif pyautogui.locateOnScreen('./img/house.png', region=(245, 12, 330, 150), confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/house.png', region=(245, 12, 330, 150), confidence=0.8))
        time.sleep(1.5)
        if pyautogui.locateOnScreen('./img/home.png', region=(50, 310, 240, 200), confidence=0.8) != None:
            pyautogui.click(pyautogui.locateOnScreen('./img/home.png', region=(50, 310, 240, 200), confidence=0.8))
            time.sleep(2)


def click_terminal():
    if pyautogui.locateOnScreen('./img/terminal.png', region=(1275, 150, 320, 200), confidence=0.6) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/terminal.png', region=(1275, 150, 320, 200), confidence=0.6))
    time.sleep(1)


def go_yato_event():
    locations = list(pyautogui.locateAllOnScreen('./img/yato_event.png', confidence=0.8))
    if locations:
        x, y, width, height = locations[0]
        pyautogui.click(x + width / 2, y + height / 2)
    time.sleep(4)
    
    
def click_main_stage():
    if pyautogui.locateOnScreen('./img/main_stage.png', region=(300, 900, 135, 150), confidence=0.6) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/main_stage.png', region=(300, 900, 135, 150), confidence=0.6)) 
    time.sleep(1)


def go_yato_stage():
    if pyautogui.locateOnScreen('./img/yato_stage.png', confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/yato_stage.png', confidence=0.8)) 
    time.sleep(1)
    
     
    
def go_ep1():
    if pyautogui.locateOnScreen('./img/act0.png', region=(160, 100, 200, 200), confidence=0.4) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/act0.png', region=(160, 100, 200, 200), confidence=0.4))
    time.sleep(1)
    
    if pyautogui.locateOnScreen('./img/episode1.png', region=(330, 500, 1400, 750), confidence=0.6) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/episode1.png', region=(330, 500, 1400, 750), confidence=0.6))
    time.sleep(2)
    
    
def go_ep4():
    if pyautogui.locateOnScreen('./img/act1.png', confidence=0.7) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/act1.png', confidence=0.7))
    time.sleep(1)
            
    if pyautogui.locateOnScreen('./img/episode4.png', confidence=0.5) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/episode4.png', confidence=0.5))
    time.sleep(2)
    
    
def go_ep10():
    if pyautogui.locateOnScreen('./img/act2-1.png', confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/act2-1.png', confidence=0.8))
    time.sleep(1)
    
    if pyautogui.locateOnScreen('./img/act2-2.png', confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/act2-2.png', confidence=0.8))
    time.sleep(1)
            
    if pyautogui.locateOnScreen('./img/episode10.png', confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/episode10.png', confidence=0.8))
    time.sleep(2)
    
    
def start_stage():
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/start_stage.png', region=(1500, 925, 400, 100), confidence=0.8) != None:
            pyautogui.click(pyautogui.locateOnScreen('./img/start_stage.png', region=(1500, 925, 400, 100), confidence=0.8))
    time.sleep(1.5)


def loop_until_no_sanity_remaining():
    
    global nb_Stage_Finished
    
    # loop while there is sanity remaining
    while pyautogui.locateOnScreen('./img/restore_potions.png', confidence=0.8) == None:
        
        if pyautogui.locateOnScreen('./img/start_stage.png', region=(1500, 925, 400, 100), confidence=0.8) != None:
            pyautogui.click(pyautogui.locateOnScreen('./img/start_stage.png', region=(1500, 925, 400, 100), confidence=0.8))
            
        time.sleep(1.5)
        
        if pyautogui.locateOnScreen('./img/restore_potions.png', confidence=0.8) != None:
            break

        if pyautogui.locateOnScreen('./img/start_mission.png', region=(1515, 715, 300, 145), confidence=0.8) != None:
            pyautogui.click(pyautogui.locateOnScreen('./img/start_mission.png', region=(1515, 715, 300, 145), confidence=0.8))

        stage_finished = False

        while stage_finished == False :
            if pyautogui.locateOnScreen('./img/stage_finished.png', region=(0, 0, 1920, 1080), confidence=0.8) != None:
                nb_Stage_Finished += 1
                print("Stage finished: " + str(nb_Stage_Finished))
                stage_finished = True
                
            elif pyautogui.locateOnScreen('./img/mission_failed.png', confidence=0.8) != None:
                print("Mission failed")
                stage_finished = True
                break
        
            time.sleep(3)

        pyautogui.click(950, 500)
        time.sleep(5)
        
    pyautogui.click(pyautogui.locateOnScreen('./img/cancel_restore.png', confidence=0.8))
    print("No sanity remaining")
    

def farm_orirock_cube():
    
    go_main_menu()
    click_terminal()
    click_main_stage()
    go_ep1()

    if pyautogui.locateOnScreen('./img/1-7.png', region=(0, 280, 1920, 100), confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/1-7.png', region=(0, 280, 1920, 100), confidence=0.8))
        
    else:
        stage_found = False
        # q is pressed to quit the loop
        while stage_found == False and keyboard.is_pressed('q') == False:
            
            pyautogui.moveTo(700, 850)
            pyautogui.dragRel(100, 0, duration=0.5)     # drag to left, works if start by the right
            
            if pyautogui.locateOnScreen('./img/1-7.png', region=(0, 280, 1920, 100), confidence=0.8) != None:
                pyautogui.click(pyautogui.locateOnScreen('./img/1-7.png', region=(0, 280, 1920, 100), confidence=0.8))
                stage_found = True

            # when 1-1 detected, drag to the right
            elif pyautogui.locateOnScreen('./img/1-1.png', region=(0, 470, 1920, 100), confidence=0.8) != None:
                while stage_found == False:
                    pyautogui.moveTo(700, 850)
                    pyautogui.dragRel(-100, 0, duration=0.5)
                    if pyautogui.locateOnScreen('./img/1-7.png', region=(0, 280, 1920, 100), confidence=0.8) != None:
                        pyautogui.click(pyautogui.locateOnScreen('./img/1-7.png', region=(0, 280, 1920, 100), confidence=0.8))
                        stage_found = True
            
    start_stage()
    loop_until_no_sanity_remaining()   
    
    
def farm_loxic_kohl():
    
    go_main_menu()
    click_terminal()
    click_main_stage()
    go_ep10()
    
    if pyautogui.locateOnScreen('./img/10-15.png', confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/10-15.png', confidence=0.8))
        
    else:
        stage_found = False
        # q is pressed to quit the loop
        while stage_found == False and keyboard.is_pressed('q') == False:
            
            pyautogui.moveTo(700, 850)
            pyautogui.dragRel(100, 0, duration=0.5)     # drag to left, works if start by the right
            
            if pyautogui.locateOnScreen('./img/10-15.png', confidence=0.8) != None:
                pyautogui.click(pyautogui.locateOnScreen('./img/10-15.png', confidence=0.8))
                stage_found = True

            # when 10-1 detected, drag to the right
            elif pyautogui.locateOnScreen('./img/10-1.png', region=(0, 420, 1920, 120), confidence=0.9) != None:
                while stage_found == False:
                    pyautogui.moveTo(700, 850)
                    pyautogui.dragRel(-100, 0, duration=0.5)
                    if pyautogui.locateOnScreen('./img/10-15.png', confidence=0.8) != None:
                        pyautogui.click(pyautogui.locateOnScreen('./img/10-15.png', confidence=0.8))
                        stage_found = True
            
    start_stage()
    loop_until_no_sanity_remaining()  
    
    
def farm_rma70_12():
        
    go_main_menu()
    click_terminal()
    click_main_stage()
    go_ep4()
    
    if pyautogui.locateOnScreen('./img/4-9.png', region=(0, 445, 1920, 120), confidence=0.9) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/4-9.png', region=(0, 445, 1920, 120), confidence=0.9))
        
    else:
        stage_found = False
        # q is pressed to quit the loop
        while stage_found == False and keyboard.is_pressed('q') == False:
            
            pyautogui.moveTo(700, 850)
            pyautogui.dragRel(100, 0, duration=0.5)     # drag to left, works if start by the right
            
            if pyautogui.locateOnScreen('./img/4-9.png', region=(0, 445, 1920, 120), confidence=0.9) != None:
                pyautogui.click(pyautogui.locateOnScreen('./img/4-9.png', region=(0, 445, 1920, 120), confidence=0.9))
                stage_found = True

            # when 4-1 detected, drag to the right
            elif pyautogui.locateOnScreen('./img/4-1.png', region=(0, 475, 1920, 120), confidence=0.8) != None:
                while stage_found == False:
                    pyautogui.moveTo(700, 850)
                    pyautogui.dragRel(-100, 0, duration=0.5)
                    if pyautogui.locateOnScreen('./img/4-9.png', region=(0, 445, 1920, 120), confidence=0.9) != None:
                        pyautogui.click(pyautogui.locateOnScreen('./img/4-9.png', region=(0, 445, 1920, 120), confidence=0.9))
                        stage_found = True
            
    start_stage()
    loop_until_no_sanity_remaining()   


def farm_manganese_ore():
   
    go_main_menu()     
    click_terminal()
    click_main_stage()
    go_ep10()
    
    if pyautogui.locateOnScreen('./img/10-16.png', region=(0, 655, 1920, 120), confidence=0.9) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/10-16.png', region=(0, 655, 1920, 120), confidence=0.9))
        
    else:
        stage_found = False
        # q is pressed to quit the loop
        while stage_found == False and keyboard.is_pressed('q') == False:
            
            pyautogui.moveTo(700, 850)
            pyautogui.dragRel(100, 0, duration=0.5)     # drag to left, works if start by the right
            
            if pyautogui.locateOnScreen('./img/10-16.png', region=(0, 655, 1920, 120), confidence=0.9) != None:
                pyautogui.click(pyautogui.locateOnScreen('./img/10-16.png', region=(0, 655, 1920, 120), confidence=0.9))
                stage_found = True

            # when 10-1 detected, drag to the right
            elif pyautogui.locateOnScreen('./img/10-1.png', region=(0, 420, 1920, 120), confidence=0.9) != None:
                while stage_found == False:
                    pyautogui.moveTo(700, 850)
                    pyautogui.dragRel(-100, 0, duration=0.5)
                    if pyautogui.locateOnScreen('./img/10-16.png', region=(0, 655, 1920, 120), confidence=0.9) != None:
                        pyautogui.click(pyautogui.locateOnScreen('./img/10-16.png', region=(0, 655, 1920, 120), confidence=0.9))
                        stage_found = True
            
    start_stage()
    loop_until_no_sanity_remaining()  
    

def farm_grindstone():
      
    go_main_menu()  
    click_terminal()
    click_main_stage()
    go_ep10()
    
    if pyautogui.locateOnScreen('./img/10-12.png', region=(0, 575, 1920, 120), confidence=0.9) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/10-12.png', region=(0, 575, 1920, 120), confidence=0.9))
        
    else:
        stage_found = False
        # q is pressed to quit the loop
        while stage_found == False and keyboard.is_pressed('q') == False:
            
            pyautogui.moveTo(700, 850)
            pyautogui.dragRel(100, 0, duration=0.5)     # drag to left, works if start by the right
            
            if pyautogui.locateOnScreen('./img/10-12.png', region=(0, 575, 1920, 120), confidence=0.9) != None:
                pyautogui.click(pyautogui.locateOnScreen('./img/10-12.png', region=(0, 575, 1920, 120), confidence=0.9))
                stage_found = True

            # when 10-1 detected, drag to the right
            elif pyautogui.locateOnScreen('./img/10-1.png', region=(0, 420, 1920, 120), confidence=0.9) != None:
                while stage_found == False:
                    pyautogui.moveTo(700, 850)
                    pyautogui.dragRel(-100, 0, duration=0.5)
                    if pyautogui.locateOnScreen('./img/10-12.png', region=(0, 575, 1920, 120), confidence=0.9) != None:
                        pyautogui.click(pyautogui.locateOnScreen('./img/10-12.png', region=(0, 575, 1920, 120), confidence=0.9))
                        stage_found = True
                        
    start_stage()
    loop_until_no_sanity_remaining()  


def farm_coagulating_gel():
    
    go_main_menu()
    click_terminal()
    click_main_stage()
    go_ep10()
    
    if pyautogui.locateOnScreen('./img/10-3.png', region=(0, 420, 1920, 120), confidence=0.95) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/10-3.png', region=(0, 420, 1920, 120), confidence=0.95))
        
    else:
        stage_found = False
        # q is pressed to quit the loop
        while stage_found == False and keyboard.is_pressed('q') == False:
            
            pyautogui.moveTo(700, 850)
            pyautogui.dragRel(100, 0, duration=0.5)     # drag to left, works if start by the right
            
            if pyautogui.locateOnScreen('./img/10-3.png', region=(0, 420, 1920, 120), confidence=0.95) != None:
                pyautogui.click(pyautogui.locateOnScreen('./img/10-3.png', region=(0, 420, 1920, 120), confidence=0.95))
                stage_found = True

            # when 10-1 detected, drag to the right
            elif pyautogui.locateOnScreen('./img/10-1.png', region=(0, 420, 1920, 120), confidence=0.9) != None:
                while stage_found == False:
                    pyautogui.moveTo(700, 850)
                    pyautogui.dragRel(-100, 0, duration=0.5)
                    if pyautogui.locateOnScreen('./img/10-3.png', region=(0, 420, 1920, 120), confidence=0.95) != None:
                        pyautogui.click(pyautogui.locateOnScreen('./img/10-3.png', region=(0, 420, 1920, 120), confidence=0.95))
                        stage_found = True
            
    start_stage()
    loop_until_no_sanity_remaining()  
    

def farm_sugar_pack():
        
    go_main_menu()
    click_terminal()
    click_main_stage()
    go_ep4()
    
    if pyautogui.locateOnScreen('./img/4-2.png', region=(0, 650, 1920, 120), confidence=0.9) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/4-2.png', region=(0, 650, 1920, 120), confidence=0.9))
        
    else:
        stage_found = False
        # q is pressed to quit the loop
        while stage_found == False and keyboard.is_pressed('q') == False:
            
            pyautogui.moveTo(700, 850)
            pyautogui.dragRel(100, 0, duration=0.5)     # drag to left, works if start by the right
            
            if pyautogui.locateOnScreen('./img/4-2.png', region=(0, 650, 1920, 120), confidence=0.9) != None:
                pyautogui.click(pyautogui.locateOnScreen('./img/4-2.png', region=(0, 650, 1920, 120), confidence=0.9))
                stage_found = True

            # when 4-1 detected, drag to the right
            elif pyautogui.locateOnScreen('./img/4-1.png', region=(0, 475, 1920, 120), confidence=0.8) != None:
                while stage_found == False:
                    pyautogui.moveTo(700, 850)
                    pyautogui.dragRel(-100, 0, duration=0.5)
                    if pyautogui.locateOnScreen('./img/4-2.png', region=(0, 650, 1920, 120), confidence=0.9) != None:
                        pyautogui.click(pyautogui.locateOnScreen('./img/4-2.png', region=(0, 650, 1920, 120), confidence=0.9))
                        stage_found = True
            
    start_stage()
    loop_until_no_sanity_remaining()  

        
def farm_oriron_cluster():
        
    go_main_menu()
    click_terminal()
    click_main_stage()
    go_ep10()
    
    if pyautogui.locateOnScreen('./img/10-11.png', region=(0, 285, 1920, 120), confidence=0.95) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/10-11.png', region=(0, 285, 1920, 120), confidence=0.95))
        
    else:
        stage_found = False
        # q is pressed to quit the loop
        while stage_found == False and keyboard.is_pressed('q') == False:
            
            pyautogui.moveTo(700, 850)
            pyautogui.dragRel(100, 0, duration=0.5)     # drag to left, works if start by the right
            
            if pyautogui.locateOnScreen('./img/10-11.png', region=(0, 285, 1920, 120), confidence=0.95) != None:
                pyautogui.click(pyautogui.locateOnScreen('./img/10-11.png', region=(0, 285, 1920, 120), confidence=0.95))
                stage_found = True

            # when 10-1 detected, drag to the right
            elif pyautogui.locateOnScreen('./img/10-1.png', region=(0, 420, 1920, 120), confidence=0.9) != None:
                while stage_found == False:
                    pyautogui.moveTo(700, 850)
                    pyautogui.dragRel(-100, 0, duration=0.5)
                    if pyautogui.locateOnScreen('./img/10-11.png', region=(0, 285, 1920, 120), confidence=0.95) != None:
                        pyautogui.click(pyautogui.locateOnScreen('./img/10-11.png', region=(0, 285, 1920, 120), confidence=0.95))
                        stage_found = True
        
    start_stage()
    loop_until_no_sanity_remaining() 
    
    
def farm_yato_stage():
    
    go_main_menu()
    go_yato_event()
    go_yato_stage()
    
    if pyautogui.locateOnScreen('./img/cf-8.png', confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/cf-8.png', confidence=0.8)) 
    time.sleep(1)
    
    start_stage()
    loop_until_no_sanity_remaining() 
        
       
# GUI        
    
# Create and configure buttons with images from the "./img/buttons" folder
button_functions = [
    farm_coagulating_gel,
    farm_grindstone,
    farm_loxic_kohl,
    farm_manganese_ore,
    farm_orirock_cube,
    farm_oriron_cluster,
    farm_rma70_12,
    farm_sugar_pack,
    farm_yato_stage
# Define function for each button
]


root = ctk.CTk()
root.title("Arknights Auto Farming Bot")

# Dark Mode Theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Create a frame to hold the buttons
frame = ctk.CTkFrame(root)
frame.pack(padx=10, pady=10)

# Create and configure buttons with images from the "./img/buttons" folder
button_images = []

img_folder = "./img/buttons"

for i, filename in enumerate(os.listdir(img_folder)):
    if filename.endswith((".webp", ".png")):
        img_path = os.path.join(img_folder, filename)
        image = Image.open(img_path)
        image.thumbnail((100, 100))  # Resize image if needed
        photo = ImageTk.PhotoImage(image)
        button = ctk.CTkButton(frame, image=photo, command=button_functions[i], text="")
        button.image = photo
        button_images.append(button)

# Arrange buttons in a grid layout (3 rows, 3 columns)
for i, button in enumerate(button_images):
    row_num, col_num = divmod(i, 3)
    button.grid(row=row_num, column=col_num, padx=10, pady=10)

root.mainloop()


