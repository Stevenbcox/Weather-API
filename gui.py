import ttkbootstrap as tb
from tkinter import StringVar
from main import fetch_weather  # Import the updated function

def run_gui():
    root = tb.Window(themename="darkly")
    root.title("Call of the Dead")
    root.geometry("350x280")

    location_var = StringVar()
    result_var = StringVar()

    btn_style = tb.Style()
    btn_style.configure("Bold.TButton", font=("Arvo", 10, "bold"))

    tb.Label(root, text="Enter City or ZIP:", font=("Arvo", 10, 'bold')).pack(pady=5)
    entry = tb.Entry(root, textvariable=location_var, font=("Arvo", 10, 'bold'))
    entry.pack(pady=3)

    btn = tb.Button(root, text="Get Weather", style="Bold.TButton", bootstyle="primary",
                    command=lambda: fetch_weather(result_var))
    btn.pack(pady=5)

    result_label = tb.Label(root, textvariable=result_var, font=("Arvo", 10, 'bold'), borderwidth=5, relief="solid", wraplength=380, justify="left")
    result_label.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    run_gui()
