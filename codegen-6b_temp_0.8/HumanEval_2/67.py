

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
        raise ValueError("number should be positive")
    integral, dec = '', ''
    last_digit = int(number)
    while last_digit != 0:
        if last_digit < 10:
            integral += str(last_digit)
        else:
            dec += str(last_digit)
        last_digit = last_digit // 10
    return float.fromhex(integral + '.' + dec)
