

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # assert number > 0  # ??

    decimals = abs(int(number - int(number)))
    number = int(number)
    while (number and number % 10 == 0) or \
         (number and number % 5 == 0) or \
         (number and number % 2 == 0):
        number //= 10
        decimals += 1

    if not number:
        return 0.0
    return (int(number) + decimals) / 10 ** decimals

