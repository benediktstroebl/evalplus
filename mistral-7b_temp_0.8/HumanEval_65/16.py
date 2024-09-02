
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    ### CAN ONLY USE THIS CODE: str() , len(), x[i], ord(), chr()

    new_string = ""
    for i in range(len(str(x))):
        if i + shift < len(str(x)):
            new_string += str(x)[i + shift]
        elif i + shift > len(str(x)):
            new_string += str(x)[i - shift]
    return new_string




