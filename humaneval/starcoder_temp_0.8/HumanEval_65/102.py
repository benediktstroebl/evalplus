
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    # Make sure x is an integer.
    x = int(x)

    # Convert x to a string and store in digits.
    digits = str(x)

    # If shift is greater than the number of digits,
    # return the digits reversed.
    if shift > len(digits):
        return digits[::-1]

    # Create a new list to store the shifted digits.
    shifted = []

    # Iterate through the digits and add them to the shifted list.
    for digit in digits:
        shifted.append(digit)

    # Iterate through the shifted digits and shift them.
    for i in range(shift):
        shifted[i] = shifted[i + shift]

    # Return the shifted digits as a string.
    return ''.join(shifted)

