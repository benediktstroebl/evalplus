

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # Decompose the number
    ipart, fpart = fraction(number)
    # If the fraction is zero, return the original number
    if fpart == 0:
        return number
    # Return the decimal part
    return fpart