

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    ipart, fpart = float('inf'), float('-inf')
    while number != ipart * 10 + fpart:
        ipart, fpart = number // 10, number % 10
        number = number // 10
    return fpart
