
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    # to check if n is a prime number or not
    flag = 0
    for i in range(2, n):
        if (n % i) == 0:
            flag = 1
            break

    # if n is a prime number
    if flag == 0:
        return x
    else:
        return y
