

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    rounded_int = math.floor(number)
    if rounded_int == number:
        return math.trunc(number)
    else:
        return round(number - rounded_int, 2)

