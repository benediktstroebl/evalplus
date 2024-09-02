
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

    def simple_power(x, n):
        # your code here
        if n == 1:
            return True
        elif n == 2:
            if x % 2 == 0:
                return True
            else:
                return False
        else:
            for k in range(1, n + 1):
                if x % n == 0:
                    return False
                else:
                    x = x / n
            return True

    return simple_power(x, n)

