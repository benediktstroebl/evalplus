def is_prime(n):
    """ Checks if a number is prime

    Args:
        n (int): Number to check if it is prime

    Returns:
        bool: True if n is prime, False otherwise
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def x_or_y(n, x, y):
    """ A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Args:
        n (int): Number to base the return value on.
        x (int): One of the values to return.
        y (int): The other value to return.

    Returns:
        int: x if n is prime, otherwise y.
    """
    if is_prime(n):
        return x
    else:
        return y