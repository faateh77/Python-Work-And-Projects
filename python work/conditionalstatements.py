# # a = 11
# # if a == 10:
# #     print("a is equal to",a)
# # else:
# #     print("a is not equal to 10")

# a = 22
# if a % 2 == 0 :
#     print(a,"number is even")
# else:
#     print(a,"number is odd")    

#calculate
eng = 76
urdu = 90
maths = 71
comp = 83
complab = 81
totalMarks = 500
obt = eng + urdu + maths + comp + complab
per = obt * 100 /totalMarks

if per >=90 and per <=100:
    print("obtained marks:" , obt)
    print("total percentage is:" , per)
    print("Grade A+")
elif per >=90 and per <=100:
    print("obtained marks:" , obt)
    print("total percentage is:" , per)
    print("Grade A")
elif per >=80 and per <=89:
    print("obtained marks:" , obt)
    print("total percentage is:" , per)
    print("Grade B")
elif per >=70 and per <=79:
    print("obtained marks:" , obt)
    print("total percentage is:" , per)
    print("Grade C")
elif per >=60 and per <=69:
    print("obtained marks:" , obt)
    print("total percentage is:" , per)
    print("Grade D")
elif per >=45 and per <=59:
    print("obtained marks:" , obt)
    print("total percentage is:" , per)
    print("Grade E")
elif per<45:
    print("obtained marks:" , obt)
    print("total percentage is:" , per)
    print("Grade F")    
else:
    print("Enter valid number")    
