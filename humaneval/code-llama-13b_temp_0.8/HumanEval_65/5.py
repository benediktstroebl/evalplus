
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    n = len(str(x))
    # this is the case where we are shifting to the left
    # i.e. shift < n
    if shift <= n:
        # convert x to a list of chars
        x = list(str(x))
        # we are going to need to shift these chars
        # split the list of chars into two parts
        # first element = left, second element = right
        left, right = x[:n-shift], x[n-shift:]
        # combine left and right
        # left needs to be reversed to preserve order
        return "".join(left[::-1]+right)
    # this is the case where we are shifting to the right
    # i.e. shift > n
    # for this case, just reverse the list
    else:
        return str(x)[::-1]
