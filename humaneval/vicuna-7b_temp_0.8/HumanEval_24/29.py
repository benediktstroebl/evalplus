

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n < 2:
        return n
    if n % 2 == 0:
        return max(largest_divisor(n//2), largest_divisor(n//2))
    if n % 3 == 0:
        return max(largest_divisor(n//3), largest_divisor(n//3))
    if n % 4 == 0:
        return max(largest_divisor(n//4), largest_divisor(n//4))
    if n % 5 == 0:
        return max(largest_divisor(n//5), largest_divisor(n//5))
    return n
