

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # Remove the positive sign
    if number < 0:
        number = -number

    integer_part, decimals_part = math.modf(number)
    # NOTE: We round the integer part to a 'high' precision, because we need
    #       to count the integer part as a decimal (as the fractions module does).
    integer_part = round(integer_part, DECIMALS)
    decimals_part = round(decimals_part, DECIMALS)

    return decimals_part

