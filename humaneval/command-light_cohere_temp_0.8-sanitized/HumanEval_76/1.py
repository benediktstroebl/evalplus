def is_simple_power(x, n):
    if n == x or n == 0:
        return True
    elif x % n == 0:
        return False
    else:
        return True