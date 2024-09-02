

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # split number into integer part and decimals part
    integer_part = int(number)
    decimals_part = number - integer_part
    # remove the integer part from the number
    # until the integer part is the only part left
    while integer_part > 1:
        integer_part, decimals_part = decimals_part, integer_part - decimals_part
    return decimals_part
