

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

    while True:
        # Find the largest number that divides both a and b without a remainder
        if a % b == 0:
            return max(a, b)

        if b % a == 0:
            # Swap a and b if b is larger
            if a > b:
                a, b = b, a

    # Return 1 if no common divisor is found
    return 1
