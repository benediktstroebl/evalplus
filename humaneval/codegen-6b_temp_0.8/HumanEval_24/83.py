

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    low = 1
    high = n

    while low <= high:
        mid = (low + high) // 2
        if n % mid == 0:
            high = mid - 1
        else:
            low = mid + 1
    return low
