

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    number_string = str(number)
    if number_string[0] == '-':
        number_string = number_string[1:]
        if number_string[0] == '0':
            return 0.0
    integer_part = int(number_string)
    decimals = float(number_string[len(integer_part):])
    return decimals
