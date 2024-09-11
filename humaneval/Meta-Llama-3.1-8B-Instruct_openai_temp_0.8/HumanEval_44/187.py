```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    
    Parameters:
    x (int): The input number to be converted.
    base (int): The target base for the conversion. Base numbers should be less than 10.
    
    Returns:
    str: The string representation of the input number in the target base.
    """
    # Handle invalid base
    if base < 2 or base > 9:
        raise ValueError("Invalid base. Base should be between 2 and 9.")
    
    # Initialize an empty string to store the result
    result = ""
    
    # Perform the conversion by repeatedly dividing the number by the base
    while x > 0:
        # Get the remainder of the division, which represents the digit in the new base
        remainder = x % base
        
        # Prepend the digit to the result string
        result = str(remainder) + result
        
        # Update the number for the next iteration
        x = x // base
    
    # Return the result string
    return result

# Test the function
print(change_base(8, 3))  # Output: 22
print(change_base(8, 2))  # Output: 1000
print(change_base(7, 2))  # Output: 111
```

This script defines a function `change_base` that takes an integer `x` and a base `base` as input and returns the string representation of `x` in the target base. It first checks if the base is valid, then repeatedly divides the number by the base to get the remainder, which represents the digit in the new base, and prepends it to the result string. Finally, it returns the result string. The script also includes test cases to verify the function's correctness.