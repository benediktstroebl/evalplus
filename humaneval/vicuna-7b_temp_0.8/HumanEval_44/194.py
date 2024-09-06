

def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    # If base is 0, return the original number
    if base == 0:
        return x
    
    # If the number is 0, return the empty string
    if x == 0:
        return ""
    
    # Get the digits in the number
    digits = list(str(x))
    
    # Convert the number to base 10
    base_10 = 0
    for digit in digits:
        base_10 = base_10 * 10 + digit
    
    # Convert the base 10 number to the desired base
    converted = str(base_10)
    for i in range(len(digits)):
        converted = converted[:i] + digits[i] * (10**(len(digits)-i-1)) + converted[i+1:]
    
    # return the string representation of the converted number
    return converted