
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
    x, n = n, x
    while n != 0:
        if n % x == 0:
            return False
        n = n // x
    return True

x = 2
for i in range(2, 500001):
    if is_simple_power(i, 1000000):
        print(i)
