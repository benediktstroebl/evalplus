
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Initialise a string to hold the result.
    result = ""
    # Convert the integer into a string and reverse the string if shift > number of
    # digits.
    original_string = str(x)
    if shift > len(original_string):
        result = str(x)[::-1]
    else:
        result = str(x)[len(original_string)-shift:] + str(x)[:len(original_string)-shift]
    return result
