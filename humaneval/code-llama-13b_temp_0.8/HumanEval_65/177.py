
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    # Check if the shift number is greater than number of digits
    # If yes, then perform a circular shift with the number of 
    # digits that are left.
    # For example, if shift is 4 and number of digits is 2, then 
    # perform a circular shift with 2.
    number_of_digits = len(str(x))
    shift = shift % number_of_digits
    
    # Create a list and store the digits of x
    # For example, if x is 123, then the list is [1, 2, 3]
    x_digits = [int(digit) for digit in str(x)]
    
    # Shift the digits left by shift number
    # For example, if shift is 1 and the list is [1, 2, 3], 
    # then the resultant list is [3, 1, 2]
    x_digits = x_digits[shift:] + x_digits[:shift]
    
    # Create a string and store the digits of x
    # For example, if shift is 1 and the list is [3, 1, 2], 
    # then the resultant string is '312'
    result = ''.join(str(digit) for digit in x_digits)
    
    # Return the result as a string
    return result
