

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisors = [1]
    while True:
        if n % divisor == 0:
            return divisor
        divisors.append(divisor)
        n += divisor
    return 1