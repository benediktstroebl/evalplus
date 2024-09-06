

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisors = [2]
    while len(divisors) < n:
        for i in range(3, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)
        n = int(n ** 0.5)
    return n