```python
def change_base(x: int, base: int) -> str:
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Args:
    x (int): The number to be converted.
    base (int): The base to which the number will be converted.
    
    Returns:
    str: The string representation of the number in the new base.
    """
    
    # Check if the base is valid
    if base < 2 or base >= 10:
        raise ValueError("Base must be between 2 and 9")
    
    # Initialize an empty string to store the result
    result = ""
    
    # Perform the conversion
    while x:
        # Append the remainder of x divided by base to the result
        result = str(x % base) + result
        # Update x to be the quotient of x divided by base
        x //= base
    
    # If the result is empty, return '0'
    if not result:
        return '0'
    
    # Return the result
    return result


# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines a function `change_base` that takes an integer `x` and a base `base` as input and returns the string representation of `x` in the new base. The function uses a while loop to repeatedly divide `x` by `base` and append the remainder to the result string. If the base is not valid, it raises a ValueError. Finally, it tests the function with the provided test cases.