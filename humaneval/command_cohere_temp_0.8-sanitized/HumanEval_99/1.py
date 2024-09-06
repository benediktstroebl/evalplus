def closest_integer(s):
    """
    Return the closest integer to the given value, rounding away from zero.

    Args:
        s (str): A string representing a number.

    Returns:
        int: The closest integer to the given value.
    """
    n = float(s)
    i = int(n)
    delta = 1.0

    if n - i == 0:
        return i

    # Determine which side of zero the number is on,
    # and adjust i and delta accordingly
    if n > i:
        i += 1
        delta = -1.0
    elif n < i:
        i -= 1
        delta = 1.0

    # Loop until the difference between n and i is less than 0.5
    while True:
        if abs(n - i) < 0.5:
            return i
        elif n > i:
            i += delta
        else:
            i -= delta
        # Loop if i becomes less than -10 or greater than 10
        # to avoid infinite looping
        if i > 10 or i < -10:
            break
    return i