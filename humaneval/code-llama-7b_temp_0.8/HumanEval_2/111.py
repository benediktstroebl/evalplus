

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # truncate the number and store it in integer variable
    # 3.56789 -> 3
    integer_part = int(number)

    # subtract the integer part from the original number
    # 3.56789 - 3 -> 0.56789
    decimal_part = number - integer_part

    # return the decimal part
    return decimal_part

