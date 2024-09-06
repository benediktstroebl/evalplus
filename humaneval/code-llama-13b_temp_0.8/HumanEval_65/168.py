
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # get the digits of the integer
    n = [int(i) for i in str(x)]
    
    # if shift is greater than number of digits, we return the digits of the integer in reverse order
    if shift >= len(n):
        return "".join([str(i) for i in n[::-1]])
    
    # get the first digits of the integer
    first_digits = n[:len(n) - shift]
    
    # get the last digits of the integer
    last_digits = n[len(n) - shift:]
    
    # return the string with the last digits first
    return "".join([str(i) for i in last_digits + first_digits])
