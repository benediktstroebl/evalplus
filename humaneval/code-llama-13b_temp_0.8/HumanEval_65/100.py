
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    strs = str(x)
    strs = list(strs)
    if shift > len(strs):
        return "".join(strs[::-1])
    else:
        strs = strs[-shift:] + strs[:-shift]
        return "".join(strs)
    # END PROBLEM 10

