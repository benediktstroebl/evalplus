
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    
    #code here
    i = 0
    k = 0
    for i in range(1,n+1):
        if n % i == 0:
            k = k + 1
    if k > 2:
        return y
    else:
        return x

