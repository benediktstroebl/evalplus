

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # Decompose the number as (integer + decimals * 10^0)
    ipart, decimals = divmod(number, 1)
    # Determine the number of digits in the decimals part
    digits = len(str(decimals))
    # Determine the number of digits in the truncated decimals part
    num_digits = int(np.log10(decimals))
    # Truncate the decimals part by subtracting 0.5 (10^num_digits)
    decimals = decimals - 0.5
    # Round the truncated decimals part to the nearest integer
    truncated_decimals = np.round(decimals).astype(int)
    return truncated_decimals / 10**num_digits
