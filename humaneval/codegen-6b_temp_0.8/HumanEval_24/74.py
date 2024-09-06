

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n <= 1:
        return n
    max_divisor = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            max_divisor = i
            current_divisor = i
            while n % current_divisor == 0:
                max_divisor = current_divisor
                n = n // current_divisor
            i += 1
    return max_divisor

