# Connor Smith
# Professor Saremi
# SSW 567
# HW 01


def classify_triangle(a, b, c):
    x = a + b + c
    sides = (a, b, c)
    a, b, c = sorted(sides)
    if x < (2 * a) or x < (2 * b) or x < (2 * c):
        return "Not a Triangle!"
    elif a == b == c:
        return "Equilateral Triangle"
    elif (a == b) or (a == c) or (b == c):
        if round(a ** 2 + b ** 2) == c ** 2:
            return "Isosceles and Right Triangle"
        else:
            return "Isosceles Triangle"
    else:
        if a ** 2 + b ** 2 == c ** 2:
            return "Scalene and Right Triangle"
        else:
            return "Scalene Triangle"
