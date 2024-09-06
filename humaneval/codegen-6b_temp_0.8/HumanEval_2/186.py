

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # 1. Find the integer part of the number
    integer_part = floor(number)

    # 2. Find the decimals
    decimal_part = number - integer_part

    # 3. Return the decimal part
    return decimal_part

