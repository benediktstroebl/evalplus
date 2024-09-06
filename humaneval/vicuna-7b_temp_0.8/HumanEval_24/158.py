

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # loop through small numbers to find the largest divisor
    divisors = [2]
    while divisors[-1] < n:
        for i in range(2, n + 1):
            if (n % i == 0) and (i <= n // i):
                divisors.append(i)
    return divisors[-1]
