
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # TO DO
    # string = str(x)
    # if len(string) > shift:
    #     return string[shift:] + string[:shift]
    # else:
    #     return string[::-1]
    string = str(x)
    x = [int(x) for x in string]
    while shift > len(x):
        shift -= len(x)
        x.append(x[0])
        x.pop(0)
    x.append(x[-1])
    x.pop(0)
    x = [str(x) for x in x]
    return "".join(x)

