

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisors = [1]
    while n > 1:
        for d in divisors:
            if d % n == 0 and d < n:
                return d
        divisors.append(divisors[-1] * 2)
        n //= 2
    
    return n