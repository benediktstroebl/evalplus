
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
    if isinstance(x,int) and isinstance(n,int):
        return True
    else:
        return False
    # check if x is an integer
    # check if n is an integer
    # check if x is a simple power of n
    # return True if x is a simple power of n and False in other cases
    # get the integer part of x
    # get the integer part of n
    # if x is an integer power of n, return True
    # else, return False
