import webbrowser
import os
import pyautogui
import time

class ListInput:
    def __init__(self):
        self.list_name = []
        self.list_wa = []

    def get_user_list_name(self):
        n = int(input("Enter number Name: "))
        for i in range(n):
            name = str(input())
            self.list_name.append(name)

    def print_user_list_name(self):
        print("User list Name:", self.list_name)

    def get_user_list_no(self):
        n2 = int(input("Enter number of Hp: "))
        for i in range(n2):
            no = str(input())
            self.list_wa.append(no)

    def print_user_list_no(self):
        print("User list No Hp:", self.list_wa)

    def pesan(self):
        pesan_list = []
        for i in range(len(self.list_name)):
            name = self.list_name[i].replace(" ", "%20")
            nohp = self.list_wa[i]
            message = "hallo {name}! ini adalah pesan otomatis tanggal=sabtu, 18 02 23".format(name=name)
            pesan = "https://api.whatsapp.com/send?phone=62{nohp}&text={message}".format(nohp=nohp, message=message)
            pesan_list.append(pesan)
        return pesan_list

list_input = ListInput()
list_input.get_user_list_name()
list_input.get_user_list_no()
pesan_list = list_input.pesan()

for url in pesan_list:
    webbrowser.open_new(url)
    time.sleep(2)

    
    pyautogui.FAILSAFE = False
    pyautogui.moveTo(947, 317)
    pyautogui.click()
    pyautogui.PAUSE = 2
    pyautogui.moveTo(927, 391)
    pyautogui.click()
    pyautogui.PAUSE = 5
    pyautogui.moveTo(1723, 981)
    pyautogui.click()
