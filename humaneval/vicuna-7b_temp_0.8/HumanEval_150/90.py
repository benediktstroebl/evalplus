
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

    # If n is prime, x is the first digit that is not a factor of n
    if not n % any(d < 10 for d in str(n)):
        return x

    # If n is not prime, y is the first digit that is not a factor of n
    if n % 10 == 0:
        return y

    # If n is composite, return a random digit from the range 0-9
    for i in range(10):
        if n % 10 == i:
            return i
