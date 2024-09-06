

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    def check(x):
        return x % n == 0 and x < n

    return max(map(check, range(2, int(n**0.5) + 1)))
