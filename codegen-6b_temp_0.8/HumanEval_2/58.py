

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    if type(number) != float:
        raise TypeError("Not a floating point number")
    if number < 0:
        raise ValueError("Number cannot be negative")
    if number < 1.0:
        return 0
    return float(int(number * 10)) / 10.0

