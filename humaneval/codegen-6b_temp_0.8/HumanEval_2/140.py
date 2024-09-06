

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # Handle negative numbers.
    if number < 0:
        number = -number
    # If number is zero, the standard truncation process cannot be applied,
    # so return zero.
    if number == 0:
        return 0
    # Handle the positive case first.
    if number > 0:
        truncated = number
        # Each next division marks the decimals.
        for _ in range(0, 10):
            truncated /= 10
            # If the result is non-zero and still higher than the given number,
            # we cannot truncate.
            if truncated > number:
                return truncated
        return 0
    # Handle the negative case first.
    else:
        # We know that the negative number is greater than zero, so we know all
        # the decimals are zero.
        return 0
