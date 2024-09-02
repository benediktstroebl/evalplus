
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n == 2 or n == 3 or n == 5 or n == 7:
        return x
    elif n == 4:
        return y

x = 34
y = 5
n = 15
assert x_or_y(n, x, y) == x
assert x_or_y(n, y, x) == y






