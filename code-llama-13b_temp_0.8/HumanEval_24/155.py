

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    return_value = 1
    for i in range(2, n + 1):
        if n % i == 0:
            return_value = i
    return return_value

