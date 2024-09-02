
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n % 2 == 0 and n > 2:
        print("%s is a composite number" %n)
    elif n == 2:
        print("%s is a prime number" %n)
    else:
        print("%s is not a prime number" %n)

