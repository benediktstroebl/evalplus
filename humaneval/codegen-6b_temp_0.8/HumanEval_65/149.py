
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    assert shift > 0
    list_of_numbers = list(map(int, str(x)))
    shifted_list = list_of_numbers[-shift:] + list_of_numbers[:-shift]
    return str(int("".join(map(str, shifted_list))))

