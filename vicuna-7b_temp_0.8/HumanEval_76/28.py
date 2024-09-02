
def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """
    # Check if n is a power of 2
    if n % 2 == 0:
        return n**int(x) == x
    else:
        # Check if n is odd and x is a power of n
        if n == int(x):
            return True
        elif x == int(x**n):
            return True
        else:
            return False