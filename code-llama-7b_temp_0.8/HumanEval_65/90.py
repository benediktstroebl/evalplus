
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # BEGIN PROBLEM 7
    num = str(x)
    digit = len(num)
    shift %= digit
    return (num[digit - shift:] + num[:digit - shift])
    # END PROBLEM 7

