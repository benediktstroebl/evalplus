**Numerical Base Conversion Script**
```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    
    Returns:
        str: String representation of the number after conversion.
    
    Raises:
        ValueError: If base is less than 2 or greater than 9.
    """
    
    # Check if base is valid (less than 10 and greater than 1)
    if not 2 <= base <= 9:
        raise ValueError("Base must be between 2 and 9")
    
    # Initialize an empty string to store the result
    result = ""
    
    # Perform the conversion
    while x:
        # Calculate the remainder of x divided by base
        remainder = x % base
        
        # Prepend the remainder as a string to the result
        result = str(remainder) + result
        
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
This script defines a function `change_base` that takes an integer `x` and a base `base` as input, and returns the string representation of `x` in the given base. The function uses a while loop to perform the conversion, and it raises a `ValueError` if the base is invalid.