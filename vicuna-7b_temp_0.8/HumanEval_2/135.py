

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # Convert the float to an integer
    i = int(number)
    # If the decimal part is greater than 0.5, it is greater than 0.5
    if number - i > 0.5:
        # If it is greater than 0.5, the remainder is greater than 0.5
        if number - i > 0.5:
            return 1
        # Otherwise, return 0
        else:
            return 0
    # Otherwise, the decimal part is less than 0.5
    else:
        return number - i