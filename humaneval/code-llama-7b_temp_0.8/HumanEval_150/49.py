
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    import math
    def is_prime(number):
        if number == 2:
            return True
        elif number % 2 == 0:
            return False
        else:
            sqrt = int(math.sqrt(number)) + 1
            for divisor in range(3, sqrt, 2):
                if number % divisor == 0:
                    return False
            return True
    if is_prime(n):
        return x
    else:
        return y

