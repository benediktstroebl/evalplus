

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisors = [1]
    while True:
        while n % divisor > 0 for divisor in divisors:
            n //= divisor
            if n == 1:
                break
        if n == 1:
            break
        divisors.append(n)
    return divisors[-2]
