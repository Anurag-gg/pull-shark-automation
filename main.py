try:
	with open("status.md" , "r") as f:
		text = f.readline()
		num = [int(x) for x in text.split() if x.isdigit()][0]
		num += 1
	
	if num<= 1024:
		with open("status.md" , 'w') as f:
			if num in range(16):
				img = "![pull-shark](images/pull-shark-default.png)"
			elif num in range(128):
				img = "![pull-shark](images/pull-shark-bronze.png)"
			elif num in range(1024):
				img = "![pull-shark](images/pull-shark-silver.png)"
			else:
				img = "![pull-shark](images/pull-shark-gold.png)"
			
			f.write(f"{num} pull requests merged")
			f.write("<br>")
			f.write("Currently:")
			f.write("<br>")
			f.write(img)
except:
	with open("status.md" , "w") as f:
		f.write("1 pull request merged")
		f.write("<br>")
		f.write("Currently:")
		f.write("<br>")
		f.write("![pull-shark](images/pull-shark-default.png)")
