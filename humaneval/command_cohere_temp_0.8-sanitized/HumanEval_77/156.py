def iscube(a):
    # Check if the integer a is a perfect cube
    b = a**(1/3)
    return round(b) == b