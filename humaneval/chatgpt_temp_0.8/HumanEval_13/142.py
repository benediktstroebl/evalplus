def greatest_common_divisor(a: int, b: int) -> int:
    """Return a greatest common divisor of two integers a and b."""
    if b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)
