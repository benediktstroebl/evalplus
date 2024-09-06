
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
    # Function to calculate n**int
    def calculate(n, int):
        return n**int

    # If x is a power of n, return True
    if calculate(n, x % n) == x:
        return True

    # If x is not a power of n, check if it's prime
    if not is_prime(n):
        return False

    # If x is not a power of n and n is prime, return False
    return not is_power(n, x)
