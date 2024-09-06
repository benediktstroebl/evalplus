

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """

    def _to_decimal_part(number: float) -> float:
        """ Return the decimal part of a given number """

        decimals_remaining = number % 1
        return decimals_remaining

    number_parts = number // 1
    return _to_decimal_part(number)

