

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    if not isinstance(number, (int, float)):
        raise TypeError("number must be a float")
    #assert isinstance(number, float)
    if number >= 0:
        # Float must be larger than zero
        return number - int(number)
    else:
        number = abs(number)
        int_part = number - int(number)
        float_part = int_part * 10 ** len(str(int_part))
        return float_part
