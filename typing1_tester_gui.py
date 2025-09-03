import tkinter as tk
import time, random

sentences = [
    "Python is a great language for beginners and experts alike.",
    "Typing fast requires practice and consistency.",
    "Artificial Intelligence is shaping the future of technology."
]

# ---------- Functions ----------
def start():
    global start_time
    entry.delete(0, tk.END)
    msg.config(text=f"Start typing, {user_name.get()}...", fg="yellow", bg="#2b2b2b")  # Normal message
    entry.focus()
    start_time = time.time()

def finish():
    elapsed = round(time.time() - start_time, 2)
    typed = entry.get()
    original = sentence.cget("text")  
    words = len(typed.split())
    speed = round(words / (elapsed / 60), 2) if elapsed > 0 else 0

    # Accuracy
    correct_chars = sum(1 for a, b in zip(typed, original) if a == b)
    acc = round(correct_chars / len(original) * 100, 2) if original else 0

    # Feedback
    if acc > 80 and speed > 20:
        feedback = f"Shabash {user_name.get()}! 👏 Excellent work!"
    else:
        feedback = f"Good try {user_name.get()} 👍. Keep practicing to improve!"

    # 🔴 Appreciation line with red background + white text
    msg.config(
        text=f"Time: {elapsed}s | Speed: {speed} WPM | Accuracy: {acc}%\n\n{feedback}",
        fg="white", bg="red"
    )

def new_sentence():
    sentence.config(text=random.choice(sentences))
    msg.config(text="Press Start to begin.", fg="yellow", bg="#2b2b2b")  # Normal message

def save_name():
    if name_entry.get().strip():
        user_name.set(name_entry.get().strip())
        name_frame.pack_forget()
        main_interface()

# ---------- Main Window ----------
root = tk.Tk()
root.title("Typing Speed Tester")
root.state("zoomed")
root.configure(bg="#2b2b2b")   # ✅ Light black background

user_name = tk.StringVar()

# Name input frame
name_frame = tk.Frame(root, bg="gray")
tk.Label(name_frame, text="Enter Your Name:", font=("Arial",20,"bold"), fg="white", bg="#2b2b2b").pack(pady=10)

# Name Entry (white background, black text)
name_entry = tk.Entry(
    name_frame, font=("Arial",18), width=40, justify="center",
    bg="white", fg="black", insertbackground="black"
)
name_entry.pack(pady=30)

tk.Button(name_frame, text="Continue", command=save_name, bg="red", fg="white", font=("Arial",15,"bold"),width='20').pack(pady=20)
name_frame.pack(expand=True)

# Main interface function
def main_interface():
    global sentence, entry, msg
    sentence = tk.Label(
        root, text=random.choice(sentences), font=("Arial",22,"italic"),
        bg="white", fg="blue",wraplength=1000, justify="center"
    )
    sentence.pack(pady=30)

    # Typing Entry (white background, black text)
    entry = tk.Entry(
        root, font=("Arial",20), width=80, justify="center",
        bg="white", fg="black", insertbackground="black"
    )
    entry.pack(pady=40)

    frame = tk.Frame(root, bg="#2b2b2b")
    frame.pack(pady=30)
    for t, c, cmd in [
        ("Start", "green", start), ("Finish", "skyblue", finish), ("New", "purple", new_sentence)
    ]:
        tk.Button(
            frame, text=t, command=cmd, bg=c, fg="white",
            font=("Arial",15,"bold"), width=15
        ).pack(side="left", padx=15)

    # Default line (not appreciation yet)
    msg = tk.Label(root, text="Press Start to begin.", font=("Arial",18,"bold"), bg="#2b2b2b", fg="yellow")
    msg.pack(pady=60)

root.mainloop()
