
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Compute length of string representation of x
    n = len(str(x))

    # Compute the start and end indices in the string representation.
    # Recall that the string representation of an integer is a string of
    # digits, from most-significant digit to least-significant digit. The
    # two beginning digits contain the sign and the leading zero, if any.
    S = str(x)
    start = shift % n
    end = n - (shift % n)

    # Compute the new value by slicing and concatenation.
    S = S[-start:] + S[:-end]

    # Convert the new value back into an integer
    return str(int(S))

