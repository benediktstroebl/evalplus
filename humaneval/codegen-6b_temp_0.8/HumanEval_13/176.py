

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    assert 0 <= a <= sys.maxsize and 0 <= b <= sys.maxsize, 'Out of range'
    divisor, _ = max(a, b) // min(a, b), min(a, b)
    return divisor * greatest_common_divisor(a % divisor, b % divisor) if a and b else max(a, b)
