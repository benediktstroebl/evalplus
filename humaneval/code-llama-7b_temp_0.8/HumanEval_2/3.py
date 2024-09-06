

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    number_parts = str(number).split(".")
    if len(number_parts) != 2:
        raise ValueError("Cannot truncate non-decimal number")
    return float("." + number_parts[1])

