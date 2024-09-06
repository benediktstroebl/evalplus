
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # BEGIN PROBLEM 6
    string = str(x)
    if shift >= len(string):
        shift %= len(string)
        return string[-shift:][::-1] + string[:-shift]
    else:
        return string[shift:] + string[:shift]
    # END PROBLEM 6
