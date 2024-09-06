

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # firstly, we identify the integer part
    integer_part = int(number)

    # secondly, we identify the decimal part
    # we know that `number` is bigger than zero, so we can fall into the
    # `if` statement below

    truncated_number = number - integer_part
    if truncated_number >= 0.5:
        # we have the `if` statement here because `truncated_number`
        # really should always be bigger than 0.5
        # however, we want to have the smallest `truncated_number`?
        #
        # => we need to have the biggest integer part
        return int(math.ceil(truncated_number))

    return int(math.floor(truncated_number))
