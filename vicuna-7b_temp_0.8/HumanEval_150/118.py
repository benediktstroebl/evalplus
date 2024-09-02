
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n % 2 != 0:
        return y

    if n % 3 != 0:
        return y

    if n % 5 != 0:
        return y

    if n % 7 != 0:
        return y

    if n == 3:
        return y

    if n == 7:
        return y

    if n > 13:
        if (n-1) % 2 == 0:
            return y

        if (n-1) % 3 == 0:
            return y

        if (n-1) % 5 == 0:
            return y

        if (n-1) % 7 == 0:
            return y

        if (n-1) % 13 == 0:
            return y

    if n > 29:
        if (n-1) % 2 == 0:
            return y

        if (n-1) % 3 == 0:
            return y

        if (n-1) % 5 == 0:
            return y

        if (n-1) % 7 == 0:
            return y

        if (n-1) % 13 == 0:
            return y

    return x

n = int(input("Enter a positive integer n: "))
x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))

if n % 2 == 0:
    x_or_y(n, x, y)
