

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisors = []
    for i in range(2, n+1):
        if n % i == 0:
            divisors.append(i)
    return max(divis
