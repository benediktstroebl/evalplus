

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """

    # For example, 3.5 is 3 and 0.5 in integer part and decimal part respectively.
    # 0.5 is the decimal part, so we return it.

    return number % 1

