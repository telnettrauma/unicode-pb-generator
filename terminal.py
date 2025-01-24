value = 50
max_value = 100

def generate():
	cutup = value / max_value
	# doesn't run if the percentage is over 100%
	if cutup > 1:
		print('Error!')
		print('Percentage is over 100%!')
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
		print(barstring)

generate()