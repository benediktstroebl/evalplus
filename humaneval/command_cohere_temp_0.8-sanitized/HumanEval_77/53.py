def iscube(a):
    # Check if the integer a is a perfect cube
    third = a ** (1/3)
    return round(third, 3) == third