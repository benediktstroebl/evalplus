

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n == 1:
        return 1
    if n == 0:
        return 0

    return_value = 1

    while return_value * return_value <= n:
        if n % return_value == 0:
            return return_value
        return_value += 1

    return return_value - 1

