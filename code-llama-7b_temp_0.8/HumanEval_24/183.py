

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Base case
    if n <= 1:
        return n
    # Recursive case
    return largest_divisor(n - 1) if n % (n - 1) else n - 1

