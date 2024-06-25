import tkinter as tk
from pynput.keyboard import Controller
import time
import pygetwindow as gw

key = Controller()
status = False
jump = False

def toggle_status():
    global status
    status = not status
    if status:
        status_label.config(text="Status: Playing")
        root.after(100, play_pause_loop)  # Start the play/pause loop
    else:
        status_label.config(text="Status: Paused")

def jump_status():
    global jump
    jump = not jump
    if jump:
        jump_label.config(text="Auto jump: On")
    else:
        jump_label.config(text="Auto jump: Off")

def play_pause_loop():
    title = get_focused_window_title()
    print(title)
    if status and title == "Idle Slayer":
        if jump:
            key.press(' ')
            key.release(' ')
        key.press('d')
        key.release('d')
    root.after(100, play_pause_loop)  # Schedule the next execution of play_pause_loop

def stop_program():
    global status
    status = False
    root.destroy()
    
def get_focused_window_title():
    try:
        active_window = gw.getActiveWindow()
        if active_window:
            return active_window.title
        else:
            return "No active window"
    except Exception as e:
        return f"Error: {e}"

# Set up the GUI
root = tk.Tk()
root.title("Play/Pause Controller")
root.geometry("200x200")

play_pause_button = tk.Button(root, text="Play/Pause", command=toggle_status)
play_pause_button.pack(pady=10)

autojump_button = tk.Button(root, text="Auto Jump", command=jump_status)
autojump_button.pack(pady=10)

status_label = tk.Label(root, text="Status: Paused")
status_label.pack(pady=5)

jump_label = tk.Label(root, text="Auto jump: Off")
jump_label.pack(pady=5)

stop_button = tk.Button(root, text="Stop", command=stop_program)
stop_button.pack(pady=10)

root.mainloop()
