
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    reversed_digits = ''

    num_of_digits = len(str(x))

    if num_of_digits < shift:
        shift = num_of_digits

    if x < 0:
        x *= -1
        negative_flag = True
    else:
        negative_flag = False

    if shift == num_of_digits:
        x = int(str(x)[::-1])

    else:
        x = int(str(x)[shift:] + str(x)[:shift])

    if negative_flag:
        x *= -1

    return str(x)

