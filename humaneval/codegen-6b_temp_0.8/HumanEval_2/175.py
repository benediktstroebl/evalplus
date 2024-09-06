

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    if number < 0.0:
        raise ValueError("Cannot truncate negative number")

    abs_number = abs(number)
    decimal_part = round(abs_number % 1, 2)
    integer_part = int(abs_number)

    return decimal_part
