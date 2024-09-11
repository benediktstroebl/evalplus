```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.
    
    Parameters:
    x (int): The number to convert.
    base (int): The target base.
    
    Returns:
    str: The string representation of the number in the target base.
    """
    
    # Initialize an empty string to store the result
    result = ""
    
    # Initialize a dictionary to store the digits
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Perform the conversion
    while x > 0:
        # Get the remainder of the division
        remainder = x % base
        
        # Append the corresponding digit to the result
        result = digits[remainder] + result
        
        # Update x for the next iteration
        x = x // base
    
    # Return the result
    return result

# Test cases
print(change_base(8, 3))   # Output: '22'
print(change_base(8, 2))   # Output: '1000'
print(change_base(7, 2))   # Output: '111'
```

This script uses a while loop to repeatedly divide the input number `x` by the target base, appending the corresponding digit to the result each time. The `digits` dictionary is used to map the remainders to their corresponding digits in the target base. The result is returned as a string after all remaining digits have been processed.