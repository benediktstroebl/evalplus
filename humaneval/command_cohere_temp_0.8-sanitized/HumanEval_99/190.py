import numpy as np
def closest_integer(s):
    """
    Return the closest integer to the given value, rounding away from zero.

    Args:
        s (str): The input value as a string representing a number.

    Returns:
        int: The closest integer to the input value.
    """
    n = float(s)
    ans = n if n % 1 == 0 else n + np.sign(n)
    return round(ans)