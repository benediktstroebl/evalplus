

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    number_as_str = str(number)
    last_point_index = number_as_str.find(".")
    if last_point_index!= -1:
        return float(number_as_str[last_point_index+1:])
    else:
        return 0.0
