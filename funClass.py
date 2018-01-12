l = []
for n in range(0, 1000):
    if (n%9==0) and (n%3!=0):
        #divisible by 9 and not a mulitple of 3
        l.append(str(n))

print (",".join(l))
