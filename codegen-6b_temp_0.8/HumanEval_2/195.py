

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # there is an intentionally reversed order of operations
    # the int must be first
    int_part = int(number)
    # then the decimals
    decimals = number - int_part
    return decimals

