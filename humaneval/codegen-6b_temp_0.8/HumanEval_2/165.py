

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    if number > 0:
        integer_part = int(number)
        decimal_part = number - integer_part
        decimal_part_truncated = decimal_part
        # Make sure the truncated number does not say any more than one decimal
        # is in it
        while not isclose(decimal_part_truncated, 0):
            decimal_part_truncated = decimal_part_truncated * 10
            #print(f"isclose(decimal_part_truncated, 0): {isclose(decimal_part_truncated, 0.0)}")
            #print(f"fabs(decimal_part_truncated): {fabs(decimal_part_truncated)}")
            if fabs(decimal_part_truncated) < 0.0001:
                #print("invalid number")
                break
        if isclose(decimal_part_truncated, 0):
            return integer_part
        else:
            return integer_part + decimal_part_truncated
    else:
        return 0


