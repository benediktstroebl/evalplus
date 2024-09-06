def iscube(a):
    # Check if the integer a is a perfect cube
    return a ** (1/3) == round(a ** (1/3))