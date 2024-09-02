

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(n, 1, -1):
        if not n % i:
            return i
    raise ValueError(f"{n} does not have a divisor smaller than itself")

