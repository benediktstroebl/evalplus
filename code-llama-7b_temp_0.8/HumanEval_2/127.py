

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # Check if the number is negative
    if number < 0:
        raise ValueError("The number can not be negative.")

    integer_part = int(number)
    decimal_part = number - integer_part

    return decimal_part

