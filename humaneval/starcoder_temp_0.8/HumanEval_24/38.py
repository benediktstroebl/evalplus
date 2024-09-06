

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # For a given number, the largest divisor is always the square root of the number
    # This is because any number divides itself evenly.
    # This is also true for numbers larger than 1.
    # Thus, we can just take the square root of the number and see what integer divides it evenly
    return n // math.isqrt(n)
