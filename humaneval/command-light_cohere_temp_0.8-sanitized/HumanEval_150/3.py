def x_or_y(n, x, y):
    """Return x if n is a prime, otherwise return y"""
    if n < 2 or n == x or n == y:
        return x