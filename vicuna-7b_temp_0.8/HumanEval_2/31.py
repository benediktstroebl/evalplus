

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # Partition the number into integer and fractional parts
    i = int(number)
    d = number - i

    # Decide if we need to round up or down
    if i >= 0.5:
        # Round up if the fractional part is 0.5 or greater
        return 1.0
    else:
        # Round down if the fractional part is less than 0.5
        return i + 0.5