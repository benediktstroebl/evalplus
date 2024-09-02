
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

    if n == 1:
        return True
    if n < 1:
        return False
    if x == 1:
        return True
    if n == 0:
        return False

    if x == 0:
        return False
    if x == n:
        return True
    if x == 1:
        return False

    if n == 2:
        return True
    if n == 3:
        return False
    if n == 4:
        return False
    if n == 5:
        return False
    if n == 6:
        return False
    if n == 7:
        return False
    if n == 8:
        return False
    if n == 9:
        return False
    if n == 10:
        return False
    if n == 11:
        return False
    if n == 12:
        return False
    if n == 13:
        return False
    if n == 14:
        return False
    if n == 15:
        return False
    if n == 16:
        return False
    if n == 17:
        return False
    if n == 18:
        return False
    if n == 19:
        return False
    if n == 20:
        return False

    if x == n**2:
        return True
    if x == n**3:
        return False
    if x == n**4:
        return False
    if x == n**5:
        return False
    if x == n**6:
        return False
    if x == n**7:
        return False
    if x == n**8:
        return False
    if x == n**9:
        return False
    if x == n**10:
        return False
    if x == n**11:
        return False
    if x == n**12:
        return False
    if x == n**13:
        return False
    if x == n**14:
        return False
    if x == n**15:
        return False
    if x == n**16:
        return False
    if x == n**17:
        return False
    if x == n**18:
        return False
    if x == n**19:
        return False
    if x == n**20:
        return False

    return is_simple_power(x, n + 1)
