
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    assert type(n) is int and n > 1
    assert type(x) is int
    assert type(y) is int
    assert x != y

    if is_prime(n):
        return x
    else:
        return y

