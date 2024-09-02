

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
        raise ValueError("number must be positive")
    # Divide the number by 10
    decimal_places = 0
    while number >= 1:
        number /= 10
        decimal_places += 1
    # Truncate the number
    big_num = int(number) * 10 ** (decimal_places - 1)
    return float(big_num) / (10 ** (decimal_places - 1))
