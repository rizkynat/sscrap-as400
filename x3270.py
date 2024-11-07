import time, sys
from py3270 import Emulator

delayt = 1    # Delay for each screen update in seconds
mylogin = 'JHONORGE1'
mypass = 'Nathamael404'
myhost = 'pub400.com:23'
screenrows = []

# Use x3270 so you can see what is going on
my3270 = Emulator(visible=True)

def wait_for_screen_update(max_wait=5):
    """Wait for the screen to update or timeout after max_wait seconds."""
    start_time = time.time()
    while time.time() - start_time < max_wait:
        if my3270.wait_for_field():
            return True
        time.sleep(0.1)  # Small delay before retrying
    return False  # Timeout if screen doesn't update in max_wait seconds

try:
    # Connect and clear the screen
    my3270.connect(myhost)
    wait_for_screen_update()
    my3270.exec_command(b"Clear")
    wait_for_screen_update()
    
    # Enter username
    my3270.send_string(mylogin)
    wait_for_screen_update()  # Wait for the screen to be ready
    
    # Move to the password field and enter password
    my3270.exec_command(b"Tab")  # Move the cursor to password field
    my3270.send_string(mypass)
    wait_for_screen_update()
    my3270.send_enter()  # Press Enter after entering the password
    wait_for_screen_update()
    my3270.send_enter()
    # Verify if the Main Menu appears
    if not my3270.string_found(1, 39, 'Main Menu'):
        sys.exit('Error: Main Menu not found')
    else:
        print('Login successfully!')
except Exception as e:
    print(f"There was a problem running the script: {e}")
