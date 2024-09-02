

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # Your code here
    #
    # Converts the number to a string
    number_as_str = str(number)
    # Finds the index of the decimal point in the string
    decimal_point_index = number_as_str.index('.')
    # Takes the part of the number after the decimal point
    return number_as_str[decimal_point_index + 1:]

