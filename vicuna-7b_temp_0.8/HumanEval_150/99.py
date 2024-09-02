
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    # If n is a prime number, x should be the first odd number less than n
    # If n is not a prime number, y should be 0
    if n % 2 == 1:
        # n is odd, so x is the first odd number less than n
        for i in range(2, n+1):
            if n % i == 0:
                break
        else:
            return x
    else:
        return y
    
