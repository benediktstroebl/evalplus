```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    
    Args:
    x (int): The number to be converted.
    base (int): The target numerical base (less than 10).
    
    Returns:
    str: The string representation of x in the target base.
    """
    # Check if base is valid (less than 10)
    if not 2 <= base < 10:
        raise ValueError("Base must be between 2 and 9 (inclusive).")
    
    # Initialize an empty string to store the result
    result = ""
    
    # Continue conversion until x is 0
    while x:
        # Calculate the remainder of x divided by base
        remainder = x % base
        # Prepend the remainder to the result
        result = str(remainder) + result
        # Update x to be the quotient of x divided by base
        x //= base
    
    return result

# Test cases
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

This script defines a `change_base` function that takes an integer `x` and a target base `base` as input. It converts the number `x` to the target base and returns the result as a string. The function includes input validation to ensure that the target base is between 2 and 9 (inclusive). The script also includes test cases to demonstrate the function's correctness.