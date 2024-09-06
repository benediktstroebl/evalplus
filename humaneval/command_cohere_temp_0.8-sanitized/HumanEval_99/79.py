def closest_integer(s):
    """
    Return the closest integer to the given value, rounding away from zero.

    Args:
        s (str): The input value as a string representing a number.

    Returns:
        int: The closest integer to the input value.
    """
    n = float(s)
    d = abs(n)
    iii = int(n)
    iii_minus = iii - 1
    iii_plus = iii + 1

    if d == 0.0:
        return iii
    elif d == 1.0:
        return iii_minus if n > 0 else iii_plus
    elif iii_minus == iii_plus:
        return iii_minus if (iii_minus + ii) % 2 else iii_plus
    else:
        return iii_minus if d < 0.5 else iii_plus