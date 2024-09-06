is_prime = {i: True for i in range(2, 10) if i % 2 == 1 and spares_distance(i)}
def spares_distance(n):
    """
    Returns True if n is prime, False otherwise, but never crashes.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.
    """
    return x if is_prime[n] else y