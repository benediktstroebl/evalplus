

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """

    # Decimals of numbers are stored in a list.
    decimals = []
    # Current decimal is the first one.
    decimal = number
    # While current decimal is not smaller than 1
    while decimal >= 1:
        # Take the decimal and remove it from the number
        decimal = decimal - decimal
        # Then add it to the list of decimals
        decimals.append(decimal)
    # Return the last decimal, which is the smallest.
    return decimals[-1]
