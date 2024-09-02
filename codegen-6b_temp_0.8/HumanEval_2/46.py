

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # Split number into integer part and decimals
    integer_part = int(number)
    decimal_part = number - integer_part

    # Remove leading zeros
    while integer_part > 1 and decimal_part == 0:
        integer_part -= 1
        decimal_part = number - integer_part

    return decimal_part

