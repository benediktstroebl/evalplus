
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    # your code here
    # if n is divisible by 2 or 3 then it is not a prime number
    if (n % 2 == 0) or (n % 3 == 0):
        return y
    else:
        return x
