
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    
    #convert number to a string
    x = str(x)
    
    #find how many digits there are
    length = len(x)
    
    #if shift is greater than the length of the number, reverse the string
    if shift > length:
        return x[::-1]
    
    #slice the string to take the last shift digits
    x = x[-shift:]
    #add the rest of the number
    return str(x + x[:length - shift])

