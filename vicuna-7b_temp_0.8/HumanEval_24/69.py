

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n < 2:
        return 1
    divisors = [2, 3, 4, 6, 9, 10, 12, 15]
    max_divisor = max(divisors)
    if n % max_divisor == 0:
        return max_divisor
    else:
        for i in range(max_divisor + 1, n + 1):
            if n % i == 0:
                return i
        return n