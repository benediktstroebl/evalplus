
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    assert isinstance(x, int), 'x must be an integer'
    assert isinstance(shift, int), 'shift must be an integer'
    assert shift >= 0, 'shift must be non-negative'
    
    # Split integer into digits, then shift digits and append them back together
    digits = list(str(x))
    for i in range(0, abs(shift)):
        if shift > 0:
            digits.append(digits.pop(0))
        else:
            digits.insert(0, digits.pop())
    return ''.join(digits)
