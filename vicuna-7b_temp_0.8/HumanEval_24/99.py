

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n < 1:
        raise ValueError("n must be positive")
    divisors = [2]
    while True:
        for i in range(2, n + 1):
            if n % i == 0:
                divisors.append(i)
        if len(divisors) == 1:
            return divisors[0]