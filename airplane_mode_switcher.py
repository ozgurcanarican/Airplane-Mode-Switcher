##@author__: Özgür Can Arıcan

import os
import time

print(
"""
Welcome to 'Airplane Mode Switcher'...

***********************************************************

This program allows you to switch the airplane mode on/off
of your android device manually(typing on keyboard) or
automatically(in determined time).

***********************************************************

Please choose the option:
    1) Manually
    2) Automatically
    3) Quit
""")

user_choise = int(input("your choise: "))
while user_choise not in [1, 2, 3]:
    user_choise = int(input("Not entered any options, please enter '1', '2' or '3: "))

if user_choise == 1:
    
    print(
    """
    When typing on keyboard:
        o: it switches airplane mode on
        x: it switches airplane mode off
        q: it ends the program 
    """)

    while True:

        user_type = str(input("type: "))
        while user_type not in ["x", "o", "q"]:
            user_type = str(input("Not entered any options, please enter 'o', 'x' or 'q': "))

        if user_type == "o":
            os.system('cmd/c "adb shell settings put global airplane_mode_on 1"')

        elif user_type == "x":
            os.system('cmd/c "adb shell settings put global airplane_mode_on 0"')

        else:
            break

elif user_choise == 2:
    
    try:
        switch_on_time = int(input("Enter how many seconds it will be switched on: "))
    except ValueError:
        switch_on_time = int(input("Entered characters or decimals, please enter it with integers: "))

    try:
        on_off_cycle = int(input("Enter how many times it will be switched on and off: "))
    except ValueError:
        on_off_cycle = int(input("Entered characters or decimals, please enter it with integers: "))

    for c in range(on_off_cycle):
        os.system('cmd/c "adb shell settings put global airplane_mode_on 1"')
        time.sleep(switch_on_time)
        os.system('cmd/c "adb shell settings put global airplane_mode_on 0"')
        time.sleep(1)
