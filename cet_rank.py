import csv


class college:

    def __init__(self, name, bname, s_max):
        self.name = name
        self.bname = bname
        self.s_max = s_max
        self.students = []


class student:

    def __init__(self, name, rank, choices):
        self.name = name
        self.rank = rank
        self.choices = choices
        self.clg = " "

colleges = []
students = []


def is_filled(clg):
    if(len(clg.students) == clg.s_max):
        return True
    else:
        return False


def allocate(stud):
        # True if allocated False if not
    global colleges

    for x in stud.choices:
        for y in colleges:
            if x == y.name:
                if not is_filled(y):
                    y.students.append(stud)
                    stud.clg = y.name
                    return True
    stud.clg = "Not allocated"
    return False


# display students ranks and allocated colleges


with open("college.txt", "r+") as file:
    rawdata = file.readlines()
    for line in rawdata:
        line = line.split()
        colleges.append(college(line[0]+line[1], line[1], int(line[2])))


with open("students.txt", "r+") as file:
    rawd = file.readlines()
    for line in rawd:
        line = line.split()
        choices = [line[i] + line[i+1] for i in range(2, len(line), 2)]
        # print(choices)
        students.append(student(line[0], int(line[1]), choices))


# Allocation of seats
for s in students:
    allocate(s)

print("Round One Results:")

for s in students:
    print(str(s.rank)+"  "+s.clg)

print("================================================")

fchoices = []

with open("round1.txt", "r+") as file:
    rawd = file.readlines()
    for line in rawd:
        fchoices.append(int(line))

for i in range(len(students)):
    # 0 means he rejects the seats
    if(fchoices[i] == 0):
        for y in colleges:
            # print(y.students)
            if students[i] in y.students:
                y.students.remove(students[i])
                students[i].choices.remove(students[i].clg)
                students[i].clg = " "

# Second round allocation
for s in students:
    if s.clg == " ":
        allocate(s)


print("Round Two Results:")

for s in students:
    print(str(s.rank)+"  "+s.clg)

print("================================================")

print("Details of the colleges with their rankers:")

for y in colleges:
    print(y.name)
    if y.students == []:
        print("No students elligible")
    for i in y.students:
        print(i.name, end=" ")
        print(" ")
    print(" ")
