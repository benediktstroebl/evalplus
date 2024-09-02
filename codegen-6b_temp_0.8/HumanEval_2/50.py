

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # NOTE: This is a copy of
    # https://github.com/python/cpython/blob/1ccca7a8d5d9d0499a243024d7c9e00d0c3d5243/Lib/decimal.py#L329
    DIGITS = _Decimal.digits
    if not DIGITS:
        raise NotImplementedError("truncate_number() is undefined for decimal module "
                                  "of this Python version")
    if not isinstance(number, Decimal):
        number = Decimal(number)
    digit_tuple, exponent = number.as_tuple()[1:]
    decimals = abs(exponent)
    # digit_tuple doesn't include any leading zeros.
    digits = len(digit_tuple)
    if decimals > digits:
        # We have leading zeros up to or past the decimal point.
        digits = decimals
    whole_digits = digits - decimals

    if whole_digits > 0:
        return _TruncatedDecimal(digit_tuple[:whole_digits])
    elif whole_digits < 0:
        return _TruncatedDecimal(digit_tuple[:whole_digits]+digit_tuple[-1])
    else:
        return _TruncatedDecimal(digit_tuple)

