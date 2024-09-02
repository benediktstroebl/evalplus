

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    """
    Convert the number into its integer part and from there into its final
    decimal part, keeping the integer part of the number without the decimal part.
    """
    if number < 1:
        raise ValueError("The number '{}' must be greater than zero".format(number))

    number_int = int(number)
    number = number - float(number_int)
    return number

