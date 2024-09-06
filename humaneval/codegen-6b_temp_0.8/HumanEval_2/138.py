

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    integer_part, dec_part = math.modf(number)

    # Truncating the integer part of the number
    # Will only be used if the number is greater than or equal to 0.
    if integer_part >= 0:
        trunc_integer_part = int(integer_part)
    else:
        trunc_integer_part = 0
    return dec_part
