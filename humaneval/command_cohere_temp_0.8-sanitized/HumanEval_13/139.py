from math import long
def greatest_common_divisor(a, b) -> long:
    """ Return a greatest common divisor of two integers a and b """
    if a == 0:
        return b
    return greatest_common_divisor(b%a, a)