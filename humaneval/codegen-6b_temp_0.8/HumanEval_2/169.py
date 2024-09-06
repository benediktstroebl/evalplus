

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # Find the integer part of the given number
    if number > 0:
        integer = int(number)
        # return the integer only
        if integer == number:
            return integer
        # remove the integer part from the number
        decimal = number - integer
        return decimal
    else:
        raise NegativeNumberError("the given number is negative")

