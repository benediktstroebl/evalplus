
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # YOUR CODE HERE
    # THIS IS A FAR FROM A BEST SOLUTION, BUT IT WORKS
    shift = shift % len(str(x))
    if shift == 0:
        return str(x)
    else:
        new_str = ''
        for i in range(shift, len(str(x)) + shift):
            new_str += str(x)[i % len(str(x))]
        return new_str

