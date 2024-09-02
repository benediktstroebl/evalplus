
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    # for i in range(2, n):
    #     if n % i == 0:
    #         return y
    
    # return x

    # another way

    return (x if n > 1 and n % 2 != 0 and n % 3 != 0 else y)

