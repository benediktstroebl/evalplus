

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # So far, the code is correct, but there is no text.
    # The point is to explain what is happening under the hood.
    #
    # A positive number:
    #   - is truncated to integer part, result is rounded to the left with rounding
    #     method "ROUND_FLOOR"
    #
    # Negative number:
    #   - is truncated to integer part with rounding method "ROUND_FLOOR",
    #     result is rounded to the right with rounding method "ROUND_CEILING".
    #
    # A zero number:
    #   - is truncated to zero with rounding method "ROUND_FLOOR"
    #
    # Not a number:
    #   - results in a TypeError
    #
    # We do not expect negative values here.
    # We do not expect any other errors.
    #
    # How it works:
    # When we truncate a number, we round it to the nearest integer.
    # If the result is negative, we round to the left (i.e. "ceiling") or
    # otherwise to the right (i.e. "floor").
    #
    # This way we can handle both positive and negative numbers
    # and also zero and not-a-number.
    #
    # Reference:
    # https://docs.python.org/3/tutorial/floatingpoint.html

    rounded = round(number, 2)  # Round to 2 decimal places

    if rounded < 0:
        return math.floor(rounded)  # Floor to the left

    return math.ceil(rounded)  # Ceil to the right

