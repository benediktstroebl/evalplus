

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    return_value = 1

    for divisor in range(2, n):
        if n % divisor == 0:
            return_value = divisor
        else:
            continue

    return return_value

