

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    max_val = n
    for i in range(2, max_val):
        if max_val % i == 0 and max_val / i > max_val:
            max_val = i
    return
