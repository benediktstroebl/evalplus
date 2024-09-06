

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    whole_part = 0
    decimal_part = number - int(number)
    if decimal_part == 0:
        return int(number)
    while decimal_part > 0:
        whole_part += 1
        decimal_part = number - int(number)
    return whole_part, decimal_part
