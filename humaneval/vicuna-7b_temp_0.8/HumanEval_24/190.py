

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # find the largest divisor
    max_div = 1
    max_val = 1
    for i in range(1, n + 1):
        if n % i == 0 and i <= max_val:
            max_val = i
            max_div = i
    return max_div
