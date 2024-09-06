def greatest_common_divisor(a, b):
    """Returns the greatest common divisor of two integers a and b."""
    while b:
        a, b = b, a % b
    return a