import pyautogui
import time
import psutil 
import keyboard
import customtkinter as ctk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import os


print(pyautogui.size())
print(pyautogui.position())

# # check if ak is running ( only check bluestacks )
# bluestacks_status = False

# for process in psutil.process_iter():
#     if process.name() == "HD-Player.exe":
#         print("Bluestacks is running")
#         bluestacks_status = True
#         break


# # disable web search in Start on Windows 11, open Group Policy (gpedit.msc) > User Configuration 
# # > Administrative Templates > Windows Components > File Explorer, open and enable the 
# # “Turn off display of recent search entries in the File Explorer search box” policy.

# if bluestacks_status == False:
#     pyautogui.press('win')
#     pyautogui.typewrite('Arknights')
#     pyautogui.press('enter')  
#     time.sleep(8) # wait for arknights to load
#     pyautogui.press('f11') # fullscreen
    
#     while bluestacks_status == False:
        
#         if pyautogui.locateOnScreen('start_menu.png', region=(850, 962, 220, 110), confidence=0.8) != None:
#             pyautogui.click(pyautogui.locateOnScreen('start_menu.png', region=(850, 962, 220, 110), confidence=0.8))
            
#         if pyautogui.locateOnScreen('start_button.png', region=(880, 737, 160, 50), confidence=0.8) != None:
#             pyautogui.click(pyautogui.locateOnScreen('start_button.png', region=(880, 737, 160, 50), confidence=0.8))
            
#         if pyautogui.locateOnScreen('terminal.png') != None:
#             bluestacks_status = True
    
    
    
# start at main menu

# select how many potions to use
# while True:
#         restore_potions = input("How many potions to use? ")
#         if restore_potions.isdigit() == True:
#             restore_potions = int(restore_potions)
#             if restore_potions >= 0:
#                 break
            
            
nb_Stage_Finished = 0


# functions

def farm_orirock_cube():
    
    if pyautogui.locateOnScreen('./img/terminal.png', region=(1350, 182, 225, 110), confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/terminal.png', region=(1350, 182, 225, 110), confidence=0.8))
    
    time.sleep(1)

    if pyautogui.locateOnScreen('./img/main_stage.png', region=(265, 975, 135, 60), confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/main_stage.png', region=(265, 975, 135, 60), confidence=0.8))
            
    time.sleep(1)

    if pyautogui.locateOnScreen('./img/act0.png', region=(160, 112, 100, 30), confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/act0.png', region=(160, 112, 100, 30), confidence=0.8))
        
    time.sleep(1)

    if pyautogui.locateOnScreen('./img/episode1.png', region=(330, 500, 1400, 750), confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/episode1.png', region=(330, 500, 1400, 750), confidence=0.8))

    time.sleep(2)

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
            
        
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/start_stage.png', region=(1500, 925, 400, 100), confidence=0.8) != None:
            pyautogui.click(pyautogui.locateOnScreen('./img/start_stage.png', region=(1500, 925, 400, 100), confidence=0.8))
            
    time.sleep(1.5)
        
    # loop while there is sanity remaining
    while pyautogui.locateOnScreen('./img/restore_potions.png', confidence=0.8) == None:
        
        if pyautogui.locateOnScreen('./img/start_stage.png', region=(1500, 925, 400, 100), confidence=0.8) != None:
            pyautogui.click(pyautogui.locateOnScreen('./img/start_stage.png', region=(1500, 925, 400, 100), confidence=0.8))
            
        time.sleep(1.5)

        if pyautogui.locateOnScreen('./img/start_mission.png', region=(1515, 715, 300, 145), confidence=0.8) != None:
            pyautogui.click(pyautogui.locateOnScreen('./img/start_mission.png', region=(1515, 715, 300, 145), confidence=0.8))

        stage_finished = False

        while stage_finished == False:
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
    
    
def farm_loxic_kohl():
    
    if pyautogui.locateOnScreen('./img/terminal.png', region=(1350, 182, 225, 110), confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/terminal.png', region=(1350, 182, 225, 110), confidence=0.8))
    
    time.sleep(1)

    if pyautogui.locateOnScreen('./img/main_stage.png', region=(265, 975, 135, 60), confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/main_stage.png', region=(265, 975, 135, 60), confidence=0.8))
            
    time.sleep(1)

    if pyautogui.locateOnScreen('./img/act2-1.png', confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/act2-1.png', confidence=0.8))
        
    time.sleep(1)
    
    if pyautogui.locateOnScreen('./img/act2-2.png', confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/act2-2.png', confidence=0.8))
        
    time.sleep(1)
            
    if pyautogui.locateOnScreen('./img/episode10.png', confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/episode10.png', confidence=0.8))
        
    time.sleep(2)
    
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
            
        
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/start_stage.png', region=(1500, 925, 400, 100), confidence=0.8) != None:
            pyautogui.click(pyautogui.locateOnScreen('./img/start_stage.png', region=(1500, 925, 400, 100), confidence=0.8))
            
    time.sleep(1.5)
        
    # loop while there is sanity remaining
    while pyautogui.locateOnScreen('./img/restore_potions.png', confidence=0.8) == None:
        
        if pyautogui.locateOnScreen('./img/start_stage.png', region=(1500, 925, 400, 100), confidence=0.8) != None:
            pyautogui.click(pyautogui.locateOnScreen('./img/start_stage.png', region=(1500, 925, 400, 100), confidence=0.8))
            
        time.sleep(1.5)

        if pyautogui.locateOnScreen('./img/start_mission.png', region=(1515, 715, 300, 145), confidence=0.8) != None:
            pyautogui.click(pyautogui.locateOnScreen('./img/start_mission.png', region=(1515, 715, 300, 145), confidence=0.8))

        stage_finished = False

        while stage_finished == False:
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
    

def farm_rma70_12():
    
    if pyautogui.locateOnScreen('./img/terminal.png', region=(1350, 182, 225, 110), confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/terminal.png', region=(1350, 182, 225, 110), confidence=0.8))
    
    time.sleep(1)

    if pyautogui.locateOnScreen('./img/main_stage.png', region=(265, 975, 135, 60), confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/main_stage.png', region=(265, 975, 135, 60), confidence=0.8))
            
    time.sleep(1)

    if pyautogui.locateOnScreen('./img/act1.png', confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/act1.png', confidence=0.8))
        
    time.sleep(1)
            
    if pyautogui.locateOnScreen('./img/episode4.png', confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/episode4.png', confidence=0.8))
        
    time.sleep(2)
    
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
            
        
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/start_stage.png', region=(1500, 925, 400, 100), confidence=0.8) != None:
            pyautogui.click(pyautogui.locateOnScreen('./img/start_stage.png', region=(1500, 925, 400, 100), confidence=0.8))
            
    time.sleep(1.5)
        
    # loop while there is sanity remaining
    while pyautogui.locateOnScreen('./img/restore_potions.png', confidence=0.8) == None:
        
        if pyautogui.locateOnScreen('./img/start_stage.png', region=(1500, 925, 400, 100), confidence=0.8) != None:
            pyautogui.click(pyautogui.locateOnScreen('./img/start_stage.png', region=(1500, 925, 400, 100), confidence=0.8))
            
        time.sleep(1.5)

        if pyautogui.locateOnScreen('./img/start_mission.png', region=(1515, 715, 300, 145), confidence=0.8) != None:
            pyautogui.click(pyautogui.locateOnScreen('./img/start_mission.png', region=(1515, 715, 300, 145), confidence=0.8))

        stage_finished = False

        while stage_finished == False:
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


def farm_manganese_ore():
    
    if pyautogui.locateOnScreen('./img/terminal.png', region=(1350, 182, 225, 110), confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/terminal.png', region=(1350, 182, 225, 110), confidence=0.8))
    
    time.sleep(1)

    if pyautogui.locateOnScreen('./img/main_stage.png', region=(265, 975, 135, 60), confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/main_stage.png', region=(265, 975, 135, 60), confidence=0.8))
            
    time.sleep(1)

    if pyautogui.locateOnScreen('./img/act2-1.png', confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/act2-1.png', confidence=0.8))
        
    time.sleep(1)
    
    if pyautogui.locateOnScreen('./img/act2-2.png', confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/act2-2.png', confidence=0.8))
        
    time.sleep(1)
            
    if pyautogui.locateOnScreen('./img/episode10.png', confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/episode10.png', confidence=0.8))
        
    time.sleep(2)
    
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
            
        
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/start_stage.png', region=(1500, 925, 400, 100), confidence=0.8) != None:
            pyautogui.click(pyautogui.locateOnScreen('./img/start_stage.png', region=(1500, 925, 400, 100), confidence=0.8))
            
    time.sleep(1.5)
        
    # loop while there is sanity remaining
    while pyautogui.locateOnScreen('./img/restore_potions.png', confidence=0.8) == None:
        
        if pyautogui.locateOnScreen('./img/start_stage.png', region=(1500, 925, 400, 100), confidence=0.8) != None:
            pyautogui.click(pyautogui.locateOnScreen('./img/start_stage.png', region=(1500, 925, 400, 100), confidence=0.8))
            
        time.sleep(1.5)

        if pyautogui.locateOnScreen('./img/start_mission.png', region=(1515, 715, 300, 145), confidence=0.8) != None:
            pyautogui.click(pyautogui.locateOnScreen('./img/start_mission.png', region=(1515, 715, 300, 145), confidence=0.8))

        stage_finished = False

        while stage_finished == False:
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
    

def farm_grindstone():
    
    if pyautogui.locateOnScreen('./img/terminal.png', region=(1350, 182, 225, 110), confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/terminal.png', region=(1350, 182, 225, 110), confidence=0.8))
    
    time.sleep(1)

    if pyautogui.locateOnScreen('./img/main_stage.png', region=(265, 975, 135, 60), confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/main_stage.png', region=(265, 975, 135, 60), confidence=0.8))
            
    time.sleep(1)

    if pyautogui.locateOnScreen('./img/act2-1.png', confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/act2-1.png', confidence=0.8))
        
    time.sleep(1)
    
    if pyautogui.locateOnScreen('./img/act2-2.png', confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/act2-2.png', confidence=0.8))
        
    time.sleep(1)
            
    if pyautogui.locateOnScreen('./img/episode10.png', confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/episode10.png', confidence=0.8))
        
    time.sleep(2)
    
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
            
        
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/start_stage.png', region=(1500, 925, 400, 100), confidence=0.8) != None:
            pyautogui.click(pyautogui.locateOnScreen('./img/start_stage.png', region=(1500, 925, 400, 100), confidence=0.8))
            
    time.sleep(1.5)
        
    # loop while there is sanity remaining
    while pyautogui.locateOnScreen('./img/restore_potions.png', confidence=0.8) == None:
        
        if pyautogui.locateOnScreen('./img/start_stage.png', region=(1500, 925, 400, 100), confidence=0.8) != None:
            pyautogui.click(pyautogui.locateOnScreen('./img/start_stage.png', region=(1500, 925, 400, 100), confidence=0.8))
            
        time.sleep(1.5)

        if pyautogui.locateOnScreen('./img/start_mission.png', region=(1515, 715, 300, 145), confidence=0.8) != None:
            pyautogui.click(pyautogui.locateOnScreen('./img/start_mission.png', region=(1515, 715, 300, 145), confidence=0.8))

        stage_finished = False

        while stage_finished == False:
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


def farm_coagulating_gel():
    
    if pyautogui.locateOnScreen('./img/terminal.png', region=(1350, 182, 225, 110), confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/terminal.png', region=(1350, 182, 225, 110), confidence=0.8))
    
    time.sleep(1)

    if pyautogui.locateOnScreen('./img/main_stage.png', region=(265, 975, 135, 60), confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/main_stage.png', region=(265, 975, 135, 60), confidence=0.8))
            
    time.sleep(1)

    if pyautogui.locateOnScreen('./img/act2-1.png', confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/act2-1.png', confidence=0.8))
        
    time.sleep(1)
    
    if pyautogui.locateOnScreen('./img/act2-2.png', confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/act2-2.png', confidence=0.8))
        
    time.sleep(1)
            
    if pyautogui.locateOnScreen('./img/episode10.png', confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/episode10.png', confidence=0.8))
        
    time.sleep(2)
    
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
            
        
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/start_stage.png', region=(1500, 925, 400, 100), confidence=0.8) != None:
            pyautogui.click(pyautogui.locateOnScreen('./img/start_stage.png', region=(1500, 925, 400, 100), confidence=0.8))
            
    time.sleep(1.5)
        
    # loop while there is sanity remaining
    while pyautogui.locateOnScreen('./img/restore_potions.png', confidence=0.8) == None:
        
        if pyautogui.locateOnScreen('./img/start_stage.png', region=(1500, 925, 400, 100), confidence=0.8) != None:
            pyautogui.click(pyautogui.locateOnScreen('./img/start_stage.png', region=(1500, 925, 400, 100), confidence=0.8))
            
        time.sleep(1.5)

        if pyautogui.locateOnScreen('./img/start_mission.png', region=(1515, 715, 300, 145), confidence=0.8) != None:
            pyautogui.click(pyautogui.locateOnScreen('./img/start_mission.png', region=(1515, 715, 300, 145), confidence=0.8))

        stage_finished = False

        while stage_finished == False:
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
    

def farm_sugar_pack():
    
    if pyautogui.locateOnScreen('./img/terminal.png', region=(1350, 182, 225, 110), confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/terminal.png', region=(1350, 182, 225, 110), confidence=0.8))
    
    time.sleep(1)

    if pyautogui.locateOnScreen('./img/main_stage.png', region=(265, 975, 135, 60), confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/main_stage.png', region=(265, 975, 135, 60), confidence=0.8))
            
    time.sleep(1)

    if pyautogui.locateOnScreen('./img/act1.png', confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/act1.png', confidence=0.8))
        
    time.sleep(1)
            
    if pyautogui.locateOnScreen('./img/episode4.png', confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/episode4.png', confidence=0.8))
        
    time.sleep(2)
    
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
            
        
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/start_stage.png', region=(1500, 925, 400, 100), confidence=0.8) != None:
            pyautogui.click(pyautogui.locateOnScreen('./img/start_stage.png', region=(1500, 925, 400, 100), confidence=0.8))
            
    time.sleep(1.5)
        
    # loop while there is sanity remaining
    while pyautogui.locateOnScreen('./img/restore_potions.png', confidence=0.8) == None:
        
        if pyautogui.locateOnScreen('./img/start_stage.png', region=(1500, 925, 400, 100), confidence=0.8) != None:
            pyautogui.click(pyautogui.locateOnScreen('./img/start_stage.png', region=(1500, 925, 400, 100), confidence=0.8))
            
        time.sleep(1.5)

        if pyautogui.locateOnScreen('./img/start_mission.png', region=(1515, 715, 300, 145), confidence=0.8) != None:
            pyautogui.click(pyautogui.locateOnScreen('./img/start_mission.png', region=(1515, 715, 300, 145), confidence=0.8))

        stage_finished = False

        while stage_finished == False:
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

        
def farm_oriron_cluster():
    
    if pyautogui.locateOnScreen('./img/terminal.png', region=(1350, 182, 225, 110), confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/terminal.png', region=(1350, 182, 225, 110), confidence=0.8))
    
    time.sleep(1)

    if pyautogui.locateOnScreen('./img/main_stage.png', region=(265, 975, 135, 60), confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/main_stage.png', region=(265, 975, 135, 60), confidence=0.8))
            
    time.sleep(1)

    if pyautogui.locateOnScreen('./img/act2-1.png', confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/act2-1.png', confidence=0.8))
        
    time.sleep(1)
    
    if pyautogui.locateOnScreen('./img/act2-2.png', confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/act2-2.png', confidence=0.8))
        
    time.sleep(1)
            
    if pyautogui.locateOnScreen('./img/episode10.png', confidence=0.8) != None:
        pyautogui.click(pyautogui.locateOnScreen('./img/episode10.png', confidence=0.8))
        
    time.sleep(2)
    
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
            
        
    time.sleep(1)
    if pyautogui.locateOnScreen('./img/start_stage.png', region=(1500, 925, 400, 100), confidence=0.8) != None:
            pyautogui.click(pyautogui.locateOnScreen('./img/start_stage.png', region=(1500, 925, 400, 100), confidence=0.8))
            
    time.sleep(1.5)
        
    # loop while there is sanity remaining
    while pyautogui.locateOnScreen('./img/restore_potions.png', confidence=0.8) == None:
        
        if pyautogui.locateOnScreen('./img/start_stage.png', region=(1500, 925, 400, 100), confidence=0.8) != None:
            pyautogui.click(pyautogui.locateOnScreen('./img/start_stage.png', region=(1500, 925, 400, 100), confidence=0.8))
            
        time.sleep(1.5)

        if pyautogui.locateOnScreen('./img/start_mission.png', region=(1515, 715, 300, 145), confidence=0.8) != None:
            pyautogui.click(pyautogui.locateOnScreen('./img/start_mission.png', region=(1515, 715, 300, 145), confidence=0.8))

        stage_finished = False

        while stage_finished == False:
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
    farm_sugar_pack
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
    if filename.endswith((".webp")):
        img_path = os.path.join(img_folder, filename)
        image = Image.open(img_path)
        image.thumbnail((100, 100))  # Resize image if needed
        photo = ImageTk.PhotoImage(image)
        button = ctk.CTkButton(frame, image=photo, command=button_functions[i], text="")
        button.image = photo
        button_images.append(button)

# Arrange buttons in a grid layout (2 rows, 4 columns)
for i, button in enumerate(button_images):
    row_num, col_num = divmod(i, 4)
    button.grid(row=row_num, column=col_num, padx=10, pady=10)

root.mainloop()


        
# # select the material to farm

# while True:
#     material = input("Which material do you want to farm?\n1: Orirock Cube\n2: Loxic Kohl\n3: RMA70-12\n4: Manganese Ore\n5: Grindstone\n6: Coagulating Gel\n7: Sugar Pack\n8: Oriron Cluster\n")
    
#     if material in ["1", "Orirock Cube", "orirock cube"]:
#         # Process the Orirock Cube
#         print("Orirock Cube selected")
#         farm_orirock_cube()        
        
#         break
    
    
#     elif material in ["2", "Loxic Kohl", "loxic kohl"]:
#         # Process the Loxic Kohl
#         print("Loxic Kohl selected")
#         farm_loxic_kohl() 
    
#         break
    
    
#     elif material in ["3", "RMA70-12", "rma70-12"]:
#         # Process the RMA70-12
#         print("RMA70-12 selected")
#         farm_rma70_12()
        
#         break
    
    
#     elif material in ["4", "Manganese Ore", "manganese ore"]:
#         # Process the Manganese Ore
#         print("Manganese Ore selected")
#         farm_manganese_ore()
    
#         break
        
    
#     elif material in ["5", "Grindstone", "grindstone"]:
#         # Process the Grindstone
#         print("Grindstone selected")
#         farm_grindstone()
    
#         break
    
    
#     elif material in ["6", "Coagulating Gel", "coagulating gel"]:
#         # Process the Coagulating Gel
#         print("Coagulating gel selected")
#         farm_coagulating_gel()      
    
#         break
        
    
#     elif material in ["7", "Sugar Pack", "sugar pack"]:
#         # Process the Sugar Pack
#         print("Sugar Pack selected")
#         farm_sugar_pack()
               
#         break
    
    
#     elif material in ["8", "Oriron Cluster", "oriron cluster"]:
#         # Process the Oriron Cluster
#         print("Oriron Cluster selected")
#         farm_oriron_cluster()    
    
#         break
    
    
#     else:
#         print("Invalid material. Please enter a valid material.")




    

