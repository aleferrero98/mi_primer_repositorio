x=0
y=0
z=0
for x in range(1, 255):
	for y in range(1,255):
		z=999997/((3*x+4)*y+4)
		if(type(z)=='int'):
			println(z)