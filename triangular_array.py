def triangular_array(orientation,ordo):
	ta=[]
	for each in range(ordo):
		ta.append([0 for i in range(ordo)])	
	
	if orientation == "l":
		for row in range(ordo): 
			for col in range(row+1):
				ta[row][col] = int(raw_input("r{0} c{1}: ".format(row,col)))

				
	elif orientation == "u":
		for row in range(ordo):
			for col in range(row, ordo): 
				ta[row][col] = int(raw_input("r{0} c{1}: ".format(row,col)))
	else:
		print "put just u or l not other!\n"
		return
				
	
	return ta
	
def transpose(a):
	for row in a:
		for col in row:
			if col == 0:
				baris = a.index(row)
				kolom = row.index(col)  
				a[baris][kolom] = a[kolom][baris]
				a[kolom][baris] = 0
				
	show_array(a)
				
def merge(arrayA, arrayB):

	arrayA_Zero = len([ each for each in arrayA[0] if each == 0])
	if arrayA_Zero > 0 :
		arrayA_Orientation = 'l'
	else:
		arrayA_Orientation = 'u'
		
	arrayB_Zero = len([ each for each in arrayB[0] if each == 0])
	if arrayB_Zero > 0:
		arrayB_Orientation = 'l'
	else:
		arrayB_Orientation = 'u'
		
	arrayA_ordo = len(arrayA[0])
	arrayB_ordo = len(arrayB[0])

	arrayC = arrayA
	# a + b , n=n-1
	if arrayA_Orientation != arrayB_Orientation and arrayB_ordo == arrayA_ordo - 1:
		b = []
		for row in arrayB:
			for col in row:
				if col != 0:
					b.append(col)
		
		for row in arrayA:
			for col in row:
				if col == 0:
					baris = arrayA.index(row)
					kolom = row.index(col)
					
					arrayC[baris][kolom] = b.pop(0)
		
		return arrayC
	#  a + b, n=n
	elif arrayA_Orientation != arrayB_Orientation and arrayB_ordo == arrayA_ordo:
		baris1 =[r for r in arrayB[0] if r != 0]+[r for r in arrayA[0] if r != 0]
		arrayC=[baris1]
		for row in range( len(arrayA)-1 ):
			arrayC.append([r for r in arrayB[row+1] if r != 0]+[r for r in arrayA[row+1] if r != 0] )
			
		return arrayC
	# a + a, n = n
	elif arrayA_Orientation == arrayB_Orientation and arrayB_ordo == arrayA_ordo:
	
		transpose(arrayB)
		show_array(arrayB)
		baris1 =[r for r in arrayA[0] if r != 0]+[r for r in arrayB[0] if r != 0]
		arrayC=[baris1]
		for row in range( len(arrayA)-1 ):
			arrayC.append([r for r in arrayA[row+1] if r != 0]+[r for r in arrayB[row+1] if r != 0] )
			
		return arrayC
		
	
 		

	
	

def show_array(a):
	print
	for row in a:
		for col in row:
			print col,
		print
	print

if __name__ == "__main__":
	orientation=""
	ordo=0
	while True:
		orientation = raw_input("Upper Triangle or Lower one? [u/l] : ")
		ordo = int(raw_input("How much its ordo? [number min 2] : "))
		print
		ta=triangular_array(orientation, ordo)
		print "array A"
		show_array(ta)
		
		print "Transposed ... "
		transpose(ta)
		
		
		
		tb = triangular_array(orientation, ordo)
		print "array B"
		show_array(tb)
		#
		print
		#print "Merged ... "
		#tc = merge(ta, tb)
		#show_array(tc)
		if raw_input("Again? [y/n] :") == "n":
			break
		
	
