
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Convert the integer to a string representation.
    # There are other ways to do this.
    s = str(x)

    # Reverse the string representation.
    # There are other ways to do this.
    s = s[::-1]

    # Extract the first shift characters from the reversed string representation.
    # There are other ways to do this.
    result = s[:shift]

    # Reverse the extracted characters.
    # There are other ways to do this.
    result = result[::-1]

    # Join the shift characters to the rest of the characters of the reversed string.
    # There are other ways to do this.
    result = s[shift:] + result

    # Convert the characters to an integer.
    # There are other ways to do this.
    result = int(result)

    return result

