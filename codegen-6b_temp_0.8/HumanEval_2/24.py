

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    assert number >= 0
    # as a float, we have to perform division using float(number)
    # then we get a float with decimal point at the same position
    # than the original value to obtain the decimal part of the number
    # as we have to return a float
    # but the remainder is always a float with a decimal point at
    # the position of the original value, so we can arthimeticly
    # truncate it to keep the decimal part
    return float(number % 1.0)

