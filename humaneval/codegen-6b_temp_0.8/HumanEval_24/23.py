

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n == 1:
        return 1
    divisors = [1]
    current = 2
    while True:
        if current >= n:
            return divisors[-1]
        if n % current == 0:
            divisors.append(current)
            n //= current
        else:
            current += 1
