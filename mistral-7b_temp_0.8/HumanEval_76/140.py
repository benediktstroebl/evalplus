
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
    # write your code here
    def simple_power(x, n):
        count = 0
        if x == 1:
            return True
        if x == n:
            return True
        while x != 1:
            x = x ** n
            count += 1
            if x == 1:
                return True
        if count != 1:
            return False
    return simple_power(x, n)
