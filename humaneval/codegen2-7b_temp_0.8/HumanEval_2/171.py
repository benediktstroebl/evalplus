

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    number_str = str(number)
    number_str_int, number_str_decimal = number_str.split('.')
    number_str_int = number_str_int.rstrip('0')
    return float(number_str_int) + float(number_str_decimal)

