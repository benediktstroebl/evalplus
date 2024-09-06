

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Check if the number is divisible by 2, 3, 4, 5, 6, 10, and 12
    if n % 12 == 0 and n % 6 == 0:
        return 12
    if n % 12 == 0:
        return 12
    if n % 3 == 0:
        return 3
    if n % 4 == 0:
        return 4
    if n % 5 == 0:
        return 5
    if n % 6 == 0:
        return 6
    if n % 10 == 0:
        return 10
    return None  # Not divisible by any of the numbers
