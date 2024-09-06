def iscube(a):
    # Check if the number is greater than 0 and equal to the cube of some int
    return a > 0 and a ** (1/3) == round(a ** (1/3))