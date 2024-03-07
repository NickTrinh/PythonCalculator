import tkinter as tk

root = tk.Tk()
root.title = ("Python Calculator")

display = tk.Entry(root, width=25, font=('Arial',16))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+', '='
]

row = 1
col = 0

for button_text in buttons:
    def command(text=button_text):
        if text == '=':
            # Evaluate the expression
            try:
                result = str(eval(display.get()))
                display.delete(0, tk.END)
                display.insert(0, result)
            except:
                display.delete(0, tk.END)
                display.insert(0, "Error")
        elif text == 'C':
            # Clear the display
            display.delete(0, tk.END)
        else:
            # Append the button text to the display
            display.insert(tk.END, text)

    tk.Button(root, text=button_text, width=5, height=2, command=lambda t=button_text: command(t)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()