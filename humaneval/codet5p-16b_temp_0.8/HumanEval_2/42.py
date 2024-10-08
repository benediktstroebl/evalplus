

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """

    if number == 0.0:
        return 0.0
    int_part = truncate_number.int_part
    decimal_part = truncate_number.decimal_part
    return round(number - int_part, decimal_part)


