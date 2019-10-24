a_class = int(input("Введите число учеников в классе 'a': "))
b_class = int(input("Введите число учеников в классе 'b': "))
c_class = int(input("Введите число учеников в классе 'c': "))

a = (a_class)
b = (b_class)
c = (c_class)

if a % 2 == 0:
    a = a//2
else:
    a = a//2+1

if b % 2 == 0:
    b = b//2
else:
    b = b//2+1

if c % 2 == 0:
    c = c//2
else:
    c = c//2+1

chairs = (a_class + b_class + c_class)
desks = (a + b + c)

print(
"\nВ классе А", a_class, "студентов, для них необходимо", a, "парт"
"\nВ классе В", b_class, "студентов, для них необходимо", b, "парт"
"\nВ классе С", c_class, "студентов, для них необходимо", c, "парт")




