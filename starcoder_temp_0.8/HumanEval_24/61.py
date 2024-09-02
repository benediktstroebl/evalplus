

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    assert type(n) == int, "input should be an integer"
    assert n > 1, "input should be greater than 1"
    x = n
    while x > 1:
        if n % x == 0:
            return x
        x -= 1
