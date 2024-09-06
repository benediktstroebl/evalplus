

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    if number < 1:
        return 0
    # We divide number by 10^max_precision, and keep track of how far we went.
    # If max_precision is 0, we know that 10^max_precision is 1, and dividing
    # by it will result in the integer part being 1.
    max_precision = int(math.log10(number))
    num_digits = max_precision + 1
    if max_precision != 0:
        max_precision = max_precision - 1
    # Round number to the right of the decimal point, then remove max_precision
    # zeroes to the left.
    rounded_number = round(number, max_precision)
    return float(str(rounded_number)[max_precision:])

