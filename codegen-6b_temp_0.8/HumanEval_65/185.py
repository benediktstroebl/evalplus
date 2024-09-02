
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    
    digits = len(str(x)) # get how many digits
    if shift > digits:
        # reversed the digits
        x_reversed = int(str(x)[::-1]) # convert to string and reverse it
        shift = shift % digits # modulo
        return str(x_reversed)[:shift] # get first digits
    else:
        x_reversed = int(str(x)[::-1]) # convert to string and reverse it
        return str(x_reversed)[shift:]
    
    