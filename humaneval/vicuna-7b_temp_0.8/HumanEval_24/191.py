

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisors = []
    while n > 1:
        for i in range(1, n + 1):
            if n % i == 0:
                divisors.append(i)
        n = divisors[0]
    return n
