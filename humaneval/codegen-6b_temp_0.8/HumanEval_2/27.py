

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    if of_float_p(number) is False:
        raise TypeError("expected float")

    MULT = 1000
    int_max = int(number)
    int_len = len(str(int_max))
    f_div = int_max % MULT
    f_rem = number - int_max
    div = MULT * (int_len + 1)
    f_rem_div = f_rem / div

    if not f_rem_div and f_rem_div == 0:
        return int_max

    f_rem_div = int(f_rem_div)
    f_rem_div = float(f_rem_div)
    decimals = int(f_rem - f_rem_div * div)

    return f_rem_div + (decimals / MULT)
