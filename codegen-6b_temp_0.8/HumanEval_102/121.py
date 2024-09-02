
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    from math import sqrt
    def is_prime(x):
        if x < 2:
            return False
        if x == 2:
            return True
        if x % 2 == 0:
            return False
        limit = int(sqrt(x)) + 1
        for divisor in range(3, limit, 2):
            if x % divisor == 0:
                return False
        return True

    if not (x > 0 and y > 0):
        return -1
    elif x > y:
        return -1
    elif x == y:
        return x
    else:
        divisors = [x for x in range(1, y+1) if is_prime(x) and x <= y]
        for divisor in divisors:
            if divisor > x and divisor <= y:
                return divisor
        return -1

