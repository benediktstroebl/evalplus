
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    # for n being prime, returns x, for other values returns y
    if is_prime(n) and n % 2 == 1:
        return x
    elif not is_prime(n) or n % 2 == 0:
        return y
    else:
        return "Invalid input"
