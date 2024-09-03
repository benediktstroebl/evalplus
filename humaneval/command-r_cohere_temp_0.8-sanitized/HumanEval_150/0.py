def is_prime(n):
    """Check if input number n is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def x_or_y(n, x, y):
    """Return x if n is prime, else return y."""
    return x if is_prime(n) else y