

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Check if n is prime
    if n % 2 == 0:
        return 2
    elif n % 3 == 0:
        return 3
    elif n % 4 == 0:
        return 4
    elif n % 5 == 0:
        return 5
    else:
        # Check if n is divisible by 6, if so return 6, otherwise check if n is divisible by 3, if so return 3, otherwise return 2
        return max(6 if n % 6 == 0 else 3 if n % 3 == 0 else 2, 15)