

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    if number < 0.0 or number >= 1.0:
        raise ValueError("number must be between 0.0 and 1.0, exclusive.")
    return number - int(number)
