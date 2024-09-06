

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    factors = [1]
    while n > 1:
        for factor in factors:
            if n % factor == 0:
                if factor != factor % n:
                    return factor
                break
        n //= factor
        factors.append(factor)
    return n