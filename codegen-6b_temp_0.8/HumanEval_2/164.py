

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    if abs(number) < 1:
        return 0
    # NOTE: The round() function always returns a float.
    #   truncate_number(1) => 1.0
    #   truncate_number(1.0) => 1
    _integer_part = int(math.floor(float(number)))
    _decimal_part = _number_to_decimal(number, _integer_part)
    return _decimal_part

