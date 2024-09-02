

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    if number == 0:
        return 0
    if number < 0:
        raise ValueError('The number should be > 0')

    int_number: int = int(number)
    decimal_part: float = number - int_number
    if decimal_part == 0.0:
        # The number is integer, so we can use only int()
        return int_number
    else:
        # The number is not integer, so we can use int() and float() (arithmetic
        # operation)
        return int(number) + int(decimal_part)

