
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    n = int(n)
    if n < 2:
        return 0

    if n % 2 == 0:
        return 0

    if n % 3 == 0:
        return 0

    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0:
            return 0

    if n > 1000000:
        if n % 5 == 0:
            return 0

    if n % 7 == 0:
        return 0

    if n % 11 == 0:
        return 0

    if n % 13 == 0:
        return 0

    if n % 17 == 0:
        return 0

    if n % 19 == 0:
        return 0

    if n % 23 == 0:
        return 0

    if n % 29 == 0:
        return 0

    if n % 31 == 0:
        return 0

    if n % 37 == 0:
        return 0

    if n % 41 == 0:
        return 0

    if n % 43 == 0:
        return 0

    if n % 47 == 0:
        return 0

    if n % 53 == 0:
        return 0

    if n % 59 == 0:
        return 0

    if n % 61 == 0:
        return 0

    if n % 67 == 0:
        return 0

    if n % 71 == 0:
        return 0

    if n % 73 == 0:
        return 0

    if n % 76 == 0:
        return 0

    if n % 79 == 0:
        return 0

    if n % 81 == 0:
        return 0

    if n % 85 ==
