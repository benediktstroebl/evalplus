

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Check for zero divisors
    if a == 0 or b == 0:
        return 0
    
    # Check for negative integers
    if not (-a < b <= a):
        return 0
    
    # Compute list of common factors
    factors = []
    while a != 0 or b != 0:
        if a % b == 0:
            factors.append(b)
            b //= b % a
        else:
            factors.append(a)
            a //= a % b
            
    # If a and b have no common factors, they have a greatest common divisor of 1
    if len(factors) == 1:
        return factors[0]
    else:
        return max(factors)
