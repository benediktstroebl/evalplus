def is_prime(n):
    """ Checks whether the given number is a prime. """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def x_or_y(n, x, y):
    """ Returns the value of x if n is a prime number, 
    otherwise returns the value of y. """
    if is_prime(n):
        return x
    else:
        return y
n = 7
x = 34
y = 12