
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Determine the size of the number of digits
    num_digits = len(str(x))
    # Shift the digits right by the number of digits
    shifted = "".join([str(int(d)) if d.isdigit() else d for d in str(x)[-num_digits:]+str(x)[-1]])
    # Determine the position of the rightmost nonzero digit
    rightmost = 0
    for d in shifted:
        if d != '0':
            rightmost += int(d)
    # Return the result as a string
    return str(int(x) + (shift - num_digits) * (rightmost % (num_digits + shift - 1)))
