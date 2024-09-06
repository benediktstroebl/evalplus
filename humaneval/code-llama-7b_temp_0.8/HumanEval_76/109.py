
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
    # find the logarithm of x
    log_x = 0
    while 10**log_x < x:
        log_x += 1
    # find the logarithm of n
    log_n = 0
    while 10**log_n < n:
        log_n += 1
    # check that log_x/log_n is integer
    return int(log_x/log_n) == log_x/log_n
