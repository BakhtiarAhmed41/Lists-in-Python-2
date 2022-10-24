# A ladder put up right against a wall will fall over unless put up at a certain angle less than
# 90 degrees. Given variables length and angle storing the length of the ladder and the  angle that  it  forms  with  the  ground  as  it  leans  against  the  wall,  write  a  Python  expression involving length and angle that computes the height reached by the ladder. Evaluate the expression for these values of length and angle:
# (a)16 feet and 75 degrees (b)20 feet and 0 degrees (c)24 feet and 45 degrees (d)24 feet and 80 degrees

import math
def height(length, degrees):
    radian = math.pi * degrees / 180

    x = math.sin(radian) * length
    return x

print("a. ", height(16, 75))
print("b. ", height(20, 0))
print("c. ", height(24, 45))
print("d. ", height(24, 80))
