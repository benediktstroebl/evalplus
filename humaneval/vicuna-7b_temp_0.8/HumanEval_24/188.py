

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    def helper(d, n):
        if n == 0:
            return d
        else:
            result = n // d
            return helper(result, n % d)
    return max(helper(2, n) for n in range(1, int(n ** 0.5) + 1))