
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if (n%1 != 0) and (n%x != 0) and (n%y != 0):
        return "Invalid input. (Make sure the input is a whole number.)"
    else:
        for i in range(2, n+1):
            if n % i == 0:
                break
            if (i == n-1):
                return x
            else:
                return y
