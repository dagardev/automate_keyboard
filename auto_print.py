import pyautogui
from pynput import keyboard

# ===== GLOBALS =====
is_paused = False

# ===== INPUT =====
choice = input("Press 'Print' to start auto print, or 'SFG' to start auto sfg: ").upper()
delay = int(input("Enter time in Milliseconds: ")) / 1000

# ===== SETUP =====
def on_pause_key(key):
    """Handle pause/resume on spacebar press"""
    global is_paused
    try:
        if key == keyboard.Key.space:
            is_paused = not is_paused
            status = "PAUSED" if is_paused else "RESUMED"
            print(f"\n>>> {status} (Press SPACE to toggle) <<<")
    except AttributeError:
        pass

def start_pause_listener():
    """Start listening for pause key"""
    listener = keyboard.Listener(on_press=on_pause_key)
    listener.start()
    print("\n>>> Press SPACE to pause/resume <<<")
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
    print("You have chosen SFG mode.")
    print("Open first excel window next 'SFG' window")
    prepare()
    start_pause_listener()
    print("SFG starting...")
    
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

# ===== MAIN =====
def main():
    """Main entry point for the automation program"""
    global choice, delay
    
    # Get user input
    choice = input("Press 'Print' to start auto print, or 'SFG' to start auto sfg: ").upper()
    delay = int(input("Enter time in Milliseconds: ")) / 1000
    
    # Execute automation mode
    if choice == 'PRINT':
        auto_print_mode()
    elif choice == 'SFG':
        auto_sfg_mode()
    else:
        print("Invalid choice. Please restart and choose either 'Print' or 'SFG'.")

if __name__ == "__main__":
    main()



