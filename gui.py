import tkinter as tk
root = tk.Tk()
root.title("Unicode PB")

global value, max_value
value = 50
max_value = 100

# changes the text in the output bar
def set_new_bar(insert):
	output_box.config(state='normal')
	output_box.delete(0, "end")
	output_box.insert(0, insert)
	output_box.config(state='disabled')

# updates the values according to ones set in text boxes
def update_from_box():
	global value, max_value
	value = float(value_box.get())
	max_value = float(max_box.get())

def generate():
	update_from_box()
	cutup = value / max_value
	# doesn't run if the percentage is over 100%
	if cutup > 1:
		set_new_bar("Error! Value is greater than max!")
	else:
		repeat_amount = cutup * 100
		looptimes = 1
		barstring = '█'
		# adds black sections to progress bar
		while looptimes < repeat_amount:
			barstring = barstring + '█'
			looptimes += 1
		# gets the decimal value
		decimal_part = repeat_amount % 1
		# adds a slight transparency depending on how much of the decimal value is there
		if decimal_part != 0:
			if decimal_part < 0.5:
				barstring = barstring + '▒'
			else:
				barstring = barstring + '▓'
		# counts the nunmber of characters in the bar
		character_count = 0
		for char in barstring:
			character_count += 1
		empty_repeat_amount = 100 - character_count
		# adds the blank space to the bar
		looptimes = 0
		while looptimes < empty_repeat_amount:
			barstring = barstring + '░'
			looptimes += 1
		set_new_bar(barstring)

# copies text to the clipboard
def copy_to_clipboard():
	root.clipboard_clear()
	root.clipboard_append(output_box.get())
	root.update()

# boxes for the settings
# value
default_value = tk.DoubleVar(value=50)
tk.Label(root, text="Value").grid(column=0, row=0)
value_box = tk.Spinbox(root, width=10, textvariable=default_value, command=generate)
value_box.grid(column=1, row=0)
# max
default_max_value = tk.DoubleVar(value=100)
tk.Label(root, text="Max").grid(column=0, row=1)
max_box = tk.Spinbox(root, width=10, textvariable=default_max_value, command=generate)
max_box.grid(column=1, row=1)

# copy to clipboard
tk.Label(root, text="Clipboard").grid(column=0, row=2)
tk.Button(root, command=copy_to_clipboard, text="Copy").grid(column=1, row=2)

output_box = tk.Entry(root, width=130, font=("Arial", 9), state='disabled')
output_box.grid(column=2, row=2)

root.mainloop()