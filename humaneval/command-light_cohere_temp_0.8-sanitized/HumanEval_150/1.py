def x_or_y(n, x, y):
    if n % x == 0 or n % y == 0:
        return y
    else:
        return x