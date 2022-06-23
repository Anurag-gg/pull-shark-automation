import os

if os.stat("status.md").st_size == 0:
	with open("status.md" , "r+") as f:
		f.write("1 pull request merged")
		f.write("<br>")
		f.write("Currently:")
		f.write("<br>")
		f.write("![pull-shark](images/pull-shark-default.png)")
else:
	with open("status.md" , "r") as f:
		text = f.readline()
		num = [int(x) for x in text.split() if x.isdigit()][0]
		num += 1
	
	with open("status.md" , 'w+') as f:
		if num in range(16):
			img = "![pull-shark](images/pull-shark-default.png)"
		elif num in range(128):
			img = "![pull-shark](images/pull-shark-bronze.png)"
		elif num in range(1024):
			img = "![pull-shark](images/pull-shark-silver.png)"
		else:
			img = "![pull-shark](images/pull-shark-gold.png)"
			num -= 1
		
		f.write(f"{num} pull requests merged")
		f.write("<br>")
		f.write("Currently:")
		f.write("<br>")
		f.write(img)
		