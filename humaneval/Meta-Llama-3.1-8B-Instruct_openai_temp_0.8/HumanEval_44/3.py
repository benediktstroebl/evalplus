**Change Base Conversion Script**
=====================================

This script changes the base of a given number `x` to a target base `base`.

```python
def change_base(x: int, base: int) -> str:
    """
    Change numerical base of input number x to base.
    
    Args:
    x (int): The number to convert.
    base (int): The target base.
    
    Returns:
    str: The string representation of the number in the target base.
    
    Raises:
    ValueError: If the target base is not in the range [2, 9].
    """
    
    # Check if the target base is valid
    if not 2 <= base <= 9:
        raise ValueError("Target base must be between 2 and 9 (inclusive).")
    
    # Initialize an empty string to store the result
    result = ""
    
    # Use a while loop to divide the number by the base and append the remainder
    while x > 0:
        # Calculate the remainder
        remainder = x % base
        
        # Append the remainder to the result (converting it to a string)
        result = str(remainder) + result
        
        # Update the number by performing integer division by the base
        x = x // base
    
    # Return the result
    return result

# Test cases
if __name__ == "__main__":
    print(change_base(8, 3))  # Output: 22
    print(change_base(8, 2))  # Output: 1000
    print(change_base(7, 2))  # Output: 111
```

This script works by repeatedly dividing the input number `x` by the target base `base` and appending the remainder to the result string. The process continues until `x` is 0. The script raises a `ValueError` if the target base is not in the valid range [2, 9].