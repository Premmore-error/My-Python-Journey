#Grade of students based on marks

marks = int(input("enter Students Marks :"))

if (marks>=90):
    Grade = "A"
elif(marks>=80 and marks<=90):
    Grade = "B"
elif(marks>=70 and marks<=80):
    Grade ="C"
elif(marks>=60 and marks<=70):
    Grade = "D"
elif(marks<60):
    Grade = "FAIL"

print("Your Grade is :", Grade)
