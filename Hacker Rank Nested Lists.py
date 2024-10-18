n = int(input())

Marks = []
Name = []
Low_Student = []

low_student = 0
high = 0
low = 0
low_2 = 0
cnt = 0

while True:
    if n <= cnt or (n <= 2 and n >= 5):
        break
    
    name = str(input())
    marks = float(input())
    
    Name.append(name)
    Marks.append(marks)
        
    cnt += 1

Marks_Sort = []

for i in range(len(Marks)):
    if Marks[i] not in Marks_Sort:
        Marks_Sort.append(Marks[i])

Marks_Sort.sort()
Name_Sort = []
Marks_Sort.remove(Marks_Sort[0])

for i in range(len(Marks)):
   if Marks[i] == Marks_Sort[0]:
       Name_Sort.append(Name[i])

Name_Sort.sort()

for i in Name_Sort:
    print(i)

