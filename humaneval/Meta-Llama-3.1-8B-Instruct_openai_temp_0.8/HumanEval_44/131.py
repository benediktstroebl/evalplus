```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    
    Args:
        x (int): The number to be converted.
        base (int): The target base. Should be less than 10.
        
    Returns:
        str: The string representation of x in base.
    """
    if not isinstance(x, int) or not isinstance(base, int):
        raise ValueError("Both x and base must be integers.")
    if not 2 <= base < 10:
        raise ValueError("Base must be between 2 and 9.")
    
    converted = ''
    while x:
        x, remainder = divmod(x, base)
        converted = str(remainder) + converted
    
    return converted

# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines a function `change_base` that converts a number `x` to a specified base `base` (between 2 and 9). It uses a while loop to continuously divide the input number by the base, appending the remainder to the result as a string. When the number is 0, the loop ends, and the result is returned. The script also includes test cases to verify the correctness of the function.