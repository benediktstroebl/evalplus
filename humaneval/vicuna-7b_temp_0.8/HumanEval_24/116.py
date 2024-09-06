

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    while True:
        divisor = 6
        while divisor <= n//2:
            if n % divisor == 0:
                break
            divisor += 2
        if n % divisor == 0:
            return divisor
