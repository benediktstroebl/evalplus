

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # Find the integer part of the number:
    digit = -1
    for i in range(len(str(number))):
        if number < 1:
            digit = i - 1
            break
        number /= 10
    return number * 10 ** digit

