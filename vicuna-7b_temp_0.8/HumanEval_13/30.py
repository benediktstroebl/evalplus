

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if a < 0 or b < 0:
        raise ValueError("Both arguments must be non-negative integers.")
    if a == 0:
        return b
    return max(greatest_common_divisor(b, x) for x in range(a + 1, abs(a)) if x % a == 0)