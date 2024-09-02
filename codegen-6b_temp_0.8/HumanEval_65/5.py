
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Initialize result
    res = []

    # While `shift` is positive
    while shift > 0:
        # Add the first digit to the end of the result
        res.append(str(x % 10))
        # Subtract the first digit of `x`
        x //= 10
        # Add 1 to `shift`
        shift -= 1

    # Add the last digit to front of the result
    res.append(str(x % 10))
    # Add the rest of the digits of `x`
    res.extend(list(str(x // 10)))

    # Return the result as a string
    return "".join(res)

