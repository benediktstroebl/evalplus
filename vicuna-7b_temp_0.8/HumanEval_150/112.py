
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

    # Use the sieve of Eratosthenes to check if n is a prime number
    # If n is a prime number, return x. Otherwise, return y.

    if n == 2:  # Handle special case of n = 2
        return 2

    if n % 2 == 0:  # Handle special case of n = 2k
        return y

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return y

    return x