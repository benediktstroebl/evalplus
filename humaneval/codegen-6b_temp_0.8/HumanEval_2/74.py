

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    if not isinstance(number, float):
        raise TypeError('The number must be a float')
    if not number >= 0.0:
        raise ValueError('The number must be positive')
    if number == 0.0:
        return 0.0
    decimals = math.ceil(math.log10(abs(number))) - 1
    return math.floor(number * 10**decimals) / float(10**decimals)

