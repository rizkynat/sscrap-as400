import time, sys
from py3270 import Emulator
import mysql.connector

delayt = 1    # Delay for each screen update in seconds
mylogin = ''
mypass = ''
myhost = 'pub400.com:23'
screenrows = []

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="sscrap_as400"
)

cursor = db.cursor()

# Query data from the database
cursor.execute("SELECT username, password FROM as400_login WHERE id=1")
user_data = cursor.fetchone()
mylogin, mypass = user_data

# visible=True => x3270 so you can see what is going on
# visible=False => s3270 background, no window/frame 
em = Emulator(visible=True)

def wait_for_screen_update(max_wait=5):
    """Wait for the screen to update or timeout after max_wait seconds."""
    start_time = time.time()
    while time.time() - start_time < max_wait:
        if em.wait_for_field():
            return True
        time.sleep(0.1)  # Small delay before retrying
    return False  # Timeout if screen doesn't update in max_wait seconds

try:
    # Connect and clear the screen
    em.connect(myhost)
    wait_for_screen_update()
    em.exec_command(b"Clear")
    wait_for_screen_update()
    # Enter username
    em.send_string(mylogin)
    wait_for_screen_update()
    # Move to the password field and enter password
    em.exec_command(b"Tab")  # Move the cursor to password field
    # Enter password
    em.send_string(mypass)
    wait_for_screen_update()
    em.send_enter()
    wait_for_screen_update()
    em.send_enter()
    # Verify if the Main Menu appears
    if em.string_found(1, 39, 'Main Menu'):
        print('Login successfully!')
    elif em.string_found(1, 33, 'Display Messages'):
        em.exec_command(b"PF(3)")
    else:
        print('Login failed!')
    print('==>6. Communications')
    em.send_string('6')
    em.send_enter()
    wait_for_screen_update()
    print('==>2. Messages')
    em.send_string('2')
    em.send_enter()
    wait_for_screen_update()
    print('==>1. Send a message')
    em.send_string('1')
    em.send_enter()
    wait_for_screen_update()
    print('Send Message Menu')
    em.send_string('Hai apa kabar kamu!')
    em.exec_command(b'Tab')
    em.send_string('JHONORGE1')
    wait_for_screen_update()
    em.send_enter()
    wait_for_screen_update()
    if not em.string_found(1, 33, 'Display Messages'):
        print('Send message failed!')
    else:
        print('Send message successfully!')
    em.send_enter()
    wait_for_screen_update()
    print('==>3. Display messages')
    em.send_string('3')
    em.send_enter()
    wait_for_screen_update()
    em.send_enter()
    wait_for_screen_update()
    if not em.string_found(1, 33, 'Display Messages'):
        print('Display all message failed!')
    else:
        print('Display all message successfully!')
    wait_for_screen_update()
    em.send_enter()
    wait_for_screen_update()
    em.exec_command(b"PF(12)")
    wait_for_screen_update()
    em.exec_command(b"PF(12)")
    wait_for_screen_update()
    em.send_string('90')
    em.send_enter()
    wait_for_screen_update()
    if not em.string_found(1, 10, 'Welcome'):
        print('Logout failed!')
    else:
        print('Logout successfully!')
except Exception as e:
    print(f"There was a problem running the script: {e}")
