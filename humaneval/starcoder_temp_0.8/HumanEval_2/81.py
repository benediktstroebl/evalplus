

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """

    # Get integer part and decimal part of number
    integer_part, decimal_part = math.modf(number)

    # We only want the decimal part
    return decimal_part
