```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    
    Args:
        x (int): Number to be converted.
        base (int): Desired numerical base (numbers are less than 10).
    
    Returns:
        str: String representation of the number in the desired base.
    """
    
    # Check if base is valid
    if not 1 <= base <= 9:
        raise ValueError("Base must be an integer between 1 and 9.")
    
    # Initialize an empty string to store the result
    result = ""
    
    # Initialize a string of digits to use for the conversion
    digits = "0123456789"
    
    # Perform the conversion
    while x > 0:
        # Get the remainder of x divided by base
        remainder = x % base
        
        # Prepend the corresponding digit to the result
        result = digits[remainder] + result
        
        # Update x to be the quotient of x divided by base
        x = x // base
    
    return result

# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines a function `change_base` that converts a number `x` to a desired base `base` (between 1 and 9). It uses a while loop to repeatedly take the remainder of `x` divided by `base` and prepend the corresponding digit to the result string. The process continues until `x` is 0, at which point the function returns the resulting string. The script also includes test cases to verify the correctness of the function.