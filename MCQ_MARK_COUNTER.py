print("-----------Welcome to the Mark Counter.-----------\n")

que_num=int(input("Enter no of Question: "))
stu_num=int(input("Enter no of student who give the Exam: "))

print()

correct_ans={}
print("Now Enter the Correct Answer.")
for i in range(1,que_num+1):
    ans=input(f"{i}=")
    correct_ans[i]=ans
print()

print(f"Correct Answer:",correct_ans)

marks={}

for i in range (stu_num):

    stu_name=input("\nEnter Student Name: ")
    print("Now enter the Answer given By student.")
    print()
    total=0
    stu_ans={}     
    wrong_ans={}
    for i in range(1,que_num+1):
        ans=input(f"{i}=")
        stu_ans[i]=ans

        if stu_ans[i]==correct_ans[i]:
            total+=1 
        else:
            wrong_ans[i]=stu_ans[i]

    marks[stu_name]=total
    
 
    print(f"\nANSWERS OF {stu_name}:",stu_ans)
    print("WRONG ANSWER:",wrong_ans)
    print(f"Total Marks out of {que_num} = {total} ")


print("\nMarks Of All Student:",marks)
print("---------------------------------Thank You.---------------------------------")