

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # get the integer part of the number and the decimal part
    integer_part = int(number)
    decimal_part = number - integer_part
    # if the decimal part is greater than 1, then we need to round it up
    if decimal_part >= 1:
        # so we can't return the decimal part because it's too big
        return 1
    else:
        # otherwise, we can return it
        return decimal_part
