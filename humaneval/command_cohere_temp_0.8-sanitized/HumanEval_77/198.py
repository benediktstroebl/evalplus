def iscube(a):
    # Check if the number is greater than 0 and equals to a power of 3
    return (a > 0) and (a**(1/3) == round(a**(1/3)) )