

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    integer_part = 0
    decimal_part = 0
    counter = 0

    for digit in str(number):
        if digit == '.':
            continue
        elif digit.isdigit():
            if counter == 0:
                integer_part = integer_part * 10 + int(digit)
            else:
                decimal_part = decimal_part * 10 + int(digit)
            counter += 1

    return decimal_part / (10 ** counter)
