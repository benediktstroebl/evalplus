

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Find the largest number that divides both a and b
    max_val = max(a, b)
    
    # Loop through the range of possible divisors
    for i in range(max_val + 1, min(a + b, 1000000000)):
        # If a and b are both divisible by i, return i
        if a % i == 0 and b % i == 0:
            return i
            
    # If no common divisor is found, return 0
    return 0