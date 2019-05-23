def input_option():			#Input and Check Book
	target_file=input("Book1  Book2  Book3 ---- : ")
	check1=0
	while check1==0:		
		if target_file=="Book1":
			fr=open('Book1.txt','r')
			check1=1
		elif target_file=="Book2":
			fr=open('Book2.txt','r')
			check1=1
		elif target_file=="Book3":
			fr=open('Book3.txt','r')
			check1=1
		else:
			target_file=input("Please Enter valid Book Name: ")
			check1=0
	input_pages(fr)
def input_pages_133t(fr):		#implemented page number info and 133t logic
	pagel=int(input("Please Enter Starting Page Number: "))
	pageu=int(input("Please Enter Ending Page Number: "))
	fw=open("NewFile.txt",'a+')
	worddict=fr.readline().split(" ")
	count=0
	for i  in range(0,((25*pageu)+1)):
		count+=1
		if count>=(25*pagel)and count<=(25*pageu):
			for j in worddict[i]:
				if j=='o' or j=='O':
					j='0'
				elif j=='a' or j=='A':
					j='4'
				elif j=='e' or j=='E':
					j='3'
				elif j=='i'or j=='I':
					j='1'
			fw.write(worddict[i])
		else:
			pass


input_option()
