

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # This is a code smell. There is no reason to assume that number does not
    # have a fractional part. There are cases when the number can be exactly
    # divided into integer and decimal. We need to catch both cases.
    if not number % 1:
        return int(number)
    else:
        return number

