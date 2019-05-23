fr1= open('Book1.txt','r')
fr2= open('Book2.txt','r')
fr3= open('Book3.txt','r')
frc = open('/home/student/Desktop/fizzbuzz-SahilKohliB00797203/fizzbuzz/openbookfinal-2019-sahilkohli9779/20k.txt','r')
fw1 = open ('bookXuniqu.list','a+')
fw2 = open ('rarewords.list','a+')
dict_check1=[]
dict_check2=[]
dict_check3=[]

for i in fr1.readline():
	dict_check1.append(i.split(" "))
for i in fr2.readline():
        dict_check2.append(i.split(" "))
for i in fr3.readline():
        dict_check3.append(i.split(" "))

for i in dict_check1:
	if i in frc.word():
		pass
	else:
		fw1.write(i)
for i in dict_check2:
        if i in frc.word():
                pass
        else:
                fw1.write(i)
for i in dict_check3:
        if i in frc.word():
                pass
        else:
                fw1.write(i)

check_dict=[]
for i in frc.readline():
	check_dict.append(i)

for i in check_dict[]:
	if i in dict_check1:
		fw2.write(i)
	elif i in dict_check2:
                fw2.write(i)
	elif i in dict_check3:
                fw2.write(i)
	else:
		pass
