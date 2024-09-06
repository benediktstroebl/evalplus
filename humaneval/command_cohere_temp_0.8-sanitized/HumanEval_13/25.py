def greatest_common_divisor(a, b):
    """Return the greatest common divisor of two integers a and b."""
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)