import os
import pyautogui
import time


class ListInput:
    def __init__(self):
        self.lst1 = []
        self.lst2 = []

    def get_user_list_name(self):
        n = int(input("Enter number Name: "))
        for i in range(n):
            name = str(input())
            self.lst1.append(name)

    def print_user_list_name(self):
        print("User list Name:", self.lst1)

    def get_user_list_no(self):
        n2 = int(input("Enter number of Hp: "))
        for i in range(n2):
            no = str(input())
            self.lst2.append(no)

    def print_user_list_no(self):
        print("User list No Hp:", self.lst2)

    def pesan(self):
        pesan_list = []
        for i in range(len(self.lst1)):
            name = self.lst1[i].replace(" ", "%20")
            nohp = self.lst2[i]
            message = "hallo {name}! ini adalah pesan otomatis tanggal=sabtu, 18 02 23".format(name=name)
            pesan = "https://api.whatsapp.com/send?phone=62{nohp}&text={message}".format(nohp=nohp, message=message)
            pesan_list.append(pesan)
        return pesan_list

list_input = ListInput()
list_input.get_user_list_name()
list_input.get_user_list_no()
pesan_list = list_input.pesan()

# Wait for the user to switch to the browser window where WhatsApp is open
time.sleep(5)



# Simulate Win+R keyboard shortcut to open the Run dialog
pyautogui.hotkey('win', 'r')
time.sleep(1)  # Wait for the Run dialog to appear

# Type "chrome" and press Enter to open Google Chrome
pyautogui.typewrite('chrome')
pyautogui.press('enter')
time.sleep(5)  # Wait for Chrome to open




    
# Loop through the pesan_list and open each message in a new tab
for pesan in pesan_list:
    # Switch to the browser window
    pyautogui.hotkey('alt', 'tab')
    time.sleep(1)
    
    # Simulate Ctrl+T keyboard shortcut to open a new tab
    pyautogui.hotkey('ctrl', 't')
    time.sleep(1)
    
    # Type the pesan URL into the Chrome browser's URL bar and press Enter
    pyautogui.typewrite(pesan)
    pyautogui.press('enter')
    time.sleep(5)  # Wait for the message to load
