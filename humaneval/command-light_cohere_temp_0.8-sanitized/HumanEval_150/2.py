def x_or_y(n, x, y):
    """Check whether n is a prime number and return x if true, otherwise return y."""
    if (n <= 1) or (n % 2 == 0) or (n % 3 == 0) or (n % 5 == 0) or (n % 7 == 0) or (n % 11 == 0) or (n % 13 == 0):
        return y
    elif n % 2 == 0:
        return x
    else:
        t = 0
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                t += 1
        if t == 0:
            return x
        return y