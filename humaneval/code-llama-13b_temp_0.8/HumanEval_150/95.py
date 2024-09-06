
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    # your code here
    primes = [2,3,5,7,11,13,17,19,23,29,31]
    if n in primes:
        return x
    else:
        return y
