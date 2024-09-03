def is_simple_power(x, n):
    """Returns True if x is a simple power of n, False otherwise.
    A simple power has integer exponent.
    """
    return x == n**int(math.log(x, n))