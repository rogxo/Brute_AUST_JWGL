f = open('password.txt', mode='w+')
day = input('day:')
gender = input("Gender(M/F):")
dic = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'X']
# 21101X

if gender == 'M':
    for i3 in range(0, 10):
        for i1 in range(0, 10):
            for i2 in range(0, 10):
                for i4 in dic:
                    password = []
                    for i in day:
                        password.append(i)
                    for i in range(4):
                        password.append('A')
                    if (i3 % 2) != 0:
                        password[2] = str(i1)
                        password[3] = str(i2)
                        password[4] = str(i3)
                        password[5] = i4
                        s = ''
                        for c in password:
                            s += c
                        f.write(s + '\n')

if gender == 'F':
    for i3 in range(0, 10):
        for i1 in range(0, 10):
            for i2 in range(0, 10):
                for i4 in dic:
                    password = []
                    for i in day:
                        password.append(i)
                    for i in range(4):
                        password.append('A')
                    if (i3 % 2) == 0:
                        password[2] = str(i1)
                        password[3] = str(i2)
                        password[4] = str(i3)
                        password[5] = i4
                        s = ''
                        for c in password:
                            s += c
                        f.write(s + '\n')

f.close()
