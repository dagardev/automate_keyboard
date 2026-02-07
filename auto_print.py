import pyautogui
from pynput import keyboard

# ===== GLOBALS =====
is_paused = False

# ===== SETUP =====
def on_pause_key(key):
    """Handle pause/resume on F3 press"""
    global is_paused
    try:
        if key == keyboard.Key.f3:
            is_paused = not is_paused
            status = "PAUSED" if is_paused else "RESUMED"
            print(f"\n>>> {status} (Press F3 to toggle) <<<")
    except AttributeError:
        pass

def start_pause_listener():
    """Start listening for pause key"""
    listener = keyboard.Listener(on_press=on_pause_key)
    listener.start()
    print("\n>>> Press F3 to pause/resume <<<")
    return listener

def prepare():
    """Countdown before starting automation"""
    print("Make sure the target windows is open and ready.")
    input("Press Enter to continue...")
    for i in range(5):
        print(f"Starting in {5 - i} seconds...")
        pyautogui.sleep(1.0)

# ===== AUTOMATION MODES =====
def auto_print_mode():
    print("You have chosen Print mode.")
    print("Open first excel window next 'Zebra Print' window")
    prepare()
    start_pause_listener()
    print("Start auto print...")
    
    while True:
        # Check if paused
        while is_paused:
            pyautogui.sleep(0.1)
        
        pyautogui.hotkey("ctrl", "c")      # copy
        pyautogui.sleep(delay)
        pyautogui.hotkey("alt", "tab")     # switch window
        pyautogui.sleep(delay)
        pyautogui.hotkey("esc")  
        pyautogui.sleep(delay)
        pyautogui.hotkey("ctrl", "v")      # paste
        pyautogui.sleep(delay)
        pyautogui.hotkey("backspace")  
        pyautogui.sleep(delay)
        pyautogui.hotkey("ctrl", "p")      # print
        pyautogui.sleep(delay)
        pyautogui.hotkey("enter")
        pyautogui.sleep(delay)
        pyautogui.hotkey("alt", "tab")     # switch back
        pyautogui.sleep(delay)
        pyautogui.hotkey("down")
        pyautogui.sleep(delay)

def auto_sfg_mode():
    print(f"You have chosen {choice} mode.")
    print(f"Open first excel window next {choice} window")
    prepare()
    start_pause_listener()
    print(f"{choice} starting...")
    
    while True:
        # Check if paused
        while is_paused:
            pyautogui.sleep(0.1)
        
        pyautogui.hotkey("ctrl", "c")      # copy
        pyautogui.sleep(delay)
        pyautogui.hotkey("alt", "tab")     # switch window
        pyautogui.sleep(delay)
        pyautogui.hotkey("ctrl", "v")      # paste
        pyautogui.sleep(delay)
        pyautogui.hotkey("enter")  
        pyautogui.sleep(delay)
        pyautogui.hotkey("enter")  
        pyautogui.sleep(delay)
        pyautogui.hotkey("alt", "tab")     # switch back
        pyautogui.sleep(delay)
        pyautogui.hotkey("down")
        pyautogui.sleep(delay)
def auto_assembly_packing_mode():
    print(f"You have chosen {choice} mode.")
    print(f"Open first excel window next 'FCA' {choice} window")
    prepare()
    start_pause_listener()
    print(f"{choice} starting...")
    
    while True:
        # Check if paused
        while is_paused:
            pyautogui.sleep(0.1)
        
        pyautogui.hotkey("ctrl", "c")      # copy
        pyautogui.sleep(delay)
        pyautogui.hotkey("alt", "tab")     # switch window
        pyautogui.sleep(delay)
        pyautogui.hotkey("ctrl", "v")      # paste
        pyautogui.sleep(delay)
        pyautogui.hotkey("enter")  
        pyautogui.sleep(delay)
        pyautogui.hotkey("alt", "tab")     # switch back
        pyautogui.sleep(delay)
        pyautogui.hotkey("right")
        pyautogui.sleep(delay)
        pyautogui.hotkey("ctrl", "c")      # copy
        pyautogui.sleep(delay)
        pyautogui.hotkey("alt", "tab")     # switch back
        pyautogui.sleep(delay)
        pyautogui.hotkey("ctrl", "v")      # paste
        pyautogui.sleep(delay)
        pyautogui.hotkey("enter")  
        pyautogui.sleep(delay)
        pyautogui.hotkey("alt", "tab")     # switch back
        pyautogui.sleep(delay)
        pyautogui.hotkey("left")
        pyautogui.sleep(delay)
        pyautogui.hotkey("down")
        pyautogui.sleep(delay)

def auto_weight_mode():
    print(f"You have chosen {choice} mode.")
    print(f"Open first excel window next {choice} window")
    prepare()
    start_pause_listener()
    print(f"{choice} starting...")
    
    while True:
        # Check if paused
        while is_paused:
            pyautogui.sleep(0.1)
        
        pyautogui.hotkey("ctrl", "c")      # copy
        pyautogui.sleep(delay)
        pyautogui.hotkey("alt", "tab")     # switch window
        pyautogui.sleep(delay)
        pyautogui.hotkey("ctrl", "v")      # paste
        pyautogui.sleep(delay)
        pyautogui.hotkey("enter")   
        pyautogui.sleep(delay)
        pyautogui.hotkey("alt", "tab")     # switch back
        pyautogui.sleep(delay)
        pyautogui.hotkey("down")
        pyautogui.sleep(delay)

# ===== MAIN =====
def main():
    """Main entry point for the automation program"""
    global choice, delay
    
    # Get user input
    choice = input("""
Press 'Print' to start auto print: 
Press 'SFG' to start auto sfg: 
Press 'Assembly' to start auto assembly: 
Press 'Packing' to start auto assembly: 
Press 'Weight' to start auto weight: """).upper()
    delay = int(input("Enter Pause time in Milliseconds: ")) / 1000
    
    # Execute automation mode
    if choice == 'PRINT':
        auto_print_mode()
    elif choice == 'SFG':
        auto_sfg_mode()
    elif choice in ('ASSEMBLY' or 'PACKING'):
        auto_assembly_packing_mode()
    elif choice == 'WEIGHT':
        auto_weight_mode()
    else:
        print("Invalid choice. Please restart and choose again.")

if __name__ == "__main__":
    main()



