

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    epsilon = 10**(-6)
    if number <= 0:
        raise ValueError('You can not truncate a negative number!')
    if number == 0:
        return 0
    if number == 1:
        return 0
    decimal_part = 0
    while number != 0:
        number *= 10
        decimal_part += 1
        number -= int(number)
    return decimal_part

