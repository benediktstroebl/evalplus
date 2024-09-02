

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisors = [1, n]
    for d in range(2, (n//2)+1):
        if n % d == 0:
            divisors.append(d)
    return max(divisors)

