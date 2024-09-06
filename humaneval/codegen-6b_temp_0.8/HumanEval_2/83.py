

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # Number to the left of the point
    left = int(number)
    # Number to the right of the point
    right = number - left

    # If the number is larger than 1, one of the two numbers is larger.
    if left + right > 1:
        return right
    else:
        return left
