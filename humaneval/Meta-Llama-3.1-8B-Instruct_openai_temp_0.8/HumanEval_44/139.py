### Change Base Function
```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.

    Parameters:
    x (int): Number to be converted
    base (int): Target numerical base

    Returns:
    str: String representation of x in the target base
    """
    
    # Special case: if x is 0, return '0'
    if x == 0:
        return '0'
    
    # Handle negative numbers
    is_negative = False
    if x < 0:
        is_negative = True
        x = -x
    
    # Initialize an empty string to store the result
    result = ''
    
    # Convert the number to the target base
    while x > 0:
        # Get the remainder of x divided by base
        remainder = x % base
        
        # Prepend the remainder to the result string
        result = str(remainder) + result
        
        # Update x to be the quotient of x divided by base
        x //= base
    
    # If the original number was negative, prepend a minus sign
    if is_negative:
        result = '-' + result
    
    return result

# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
print(change_base(0, 10)) # Output: '0'
```
This code defines a function `change_base` that takes an integer `x` and a target base `base` as input, and returns a string representation of `x` in the target base. It handles negative numbers, zero, and bases less than 10. The test cases at the end demonstrate its usage.