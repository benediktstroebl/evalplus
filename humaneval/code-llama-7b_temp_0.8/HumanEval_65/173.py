
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # BEGIN PROBLEM 2
    num_len = len(str(x))
    if num_len <= shift:
        return str(x)[::-1]
    else:
        # BUG: this is not the most efficient way of achieving this
        return str(x)[shift % num_len:num_len] + str(x)[:shift % num_len]
    # END PROBLEM 2

