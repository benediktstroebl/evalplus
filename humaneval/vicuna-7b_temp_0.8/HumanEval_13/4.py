

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Iterate through the gcd of each possible pair of values in the range
    # between a and b
    for i in range(a, b+1):
        for j in range(i+1, b+1):
            # Calculate the gcd of a and j
            while j % i != 0:
                i = i - 1
                j = j + (i // 2)
            gcd = i
            # If gcd is not equal to 1, it must be greater than both a and b
            # so return gcd
            if gcd != 1:
                return gcd
    # If no gcd is found, return 1
    return 1
