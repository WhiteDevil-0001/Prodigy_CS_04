# Basic Keylogger

This Python keylogger records and logs keystrokes and saves them to a file. The program uses the `pynput` library to capture keyboard input in real-time. **Note:** Use this program ethically and only on devices where you have explicit permission. Unauthorized use of keyloggers is illegal in many countries.

## Features

- **Logs keystrokes**: Captures all keypresses, including characters and special keys.
- **Saves to file**: All recorded keystrokes are saved to a `key_log.txt` file for later review.
- **Handles special keys**: Special keys like `Ctrl`, `Shift`, `Enter` are identified and logged separately.

## Prerequisites

- Python 3.x
- `pynput` library

You can install the required library using `pip`:
pip install pynput

## How to Run
1. Clone the repository or download the code to your local machine:
    git clone https://github.com/yourusernameWhiteDevil-0001/Prodigy_CS_04.git

2. Navigate to the directory:
    cd Prodigy_CS_04

3. Run the keylogger:
    python keylogger.py

4. Stop the keylogger: You can stop the keylogger by manually closing the terminal or stopping the Python process (usually by pressing Ctrl + C).

## Output
All captured keystrokes will be logged in a file named key_log.txt in the same directory as the script. Example log format:
    hello [Key.space] world [Key.enter]

## Ethical Considerations
This tool must be used only for ethical purposes such as:

- Monitoring your own devices.
- Educational purposes (learning how keyloggers work).

## Important:
- Do not use this tool for unauthorized keylogging.
- Always obtain explicit consent from the owner of the device where the keylogger is installed.
- Unauthorized keylogging is illegal in many jurisdictions and can result in serious consequences.