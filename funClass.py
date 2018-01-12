l = []
for n in range(0, 1000):
    if (n%7==0) and (n%5!=0):
        #divisible by 7 and not a mulitple of 5
        l.append(str(n))

print (",".join(l))
