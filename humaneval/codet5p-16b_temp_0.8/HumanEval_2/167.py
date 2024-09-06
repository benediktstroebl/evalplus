

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """

    
    decimals = 0
    while number >= 1 and number < 1.1:
        number *= 10
        decimals += 1
    return number - int(number)
    
