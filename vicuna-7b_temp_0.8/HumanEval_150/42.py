
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    # Perform primality test for x
    if n < 2 or not n%2 == 0 or n%3 == 0:
        return x
    # Perform primality test for y
    if n < 3 or not (n%2 == 0 and n%5 == 0) or (n > 14 and n%7 == 1):
        return y
    # Check if n is a prime number
    if not n%2 == 0:
        return n-2
    # Check if n is a prime number
    if n > 3 and n%3 == 0:
        return n-3
    # Check if n is a prime number
    if n > 5 and n%5 == 0:
        return n-5
    # Check if n is a prime number
    if n > 14 and n%7 == 1:
        return n-7
