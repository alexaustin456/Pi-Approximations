import math
pi = float(0)
for x in range (1, 10000000):
    pi += 1.0/float(x)**2.0

pi = math.sqrt(pi*6)
print(pi)



