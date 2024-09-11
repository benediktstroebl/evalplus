### Numerical Base Conversion Script
```python
def change_base(x: int, base: int) -> str:
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.
    
    Parameters:
    x (int): The number to be converted.
    base (int): The target base.
    
    Returns:
    str: The string representation of x in the target base.
    """
    
    # Check if the base is valid
    if base < 2 or base > 9:
        raise ValueError("Base must be between 2 and 9.")
    
    # Convert the number to the target base
    if x < base:
        return str(x)
    else:
        return change_base(x // base, base) + str(x % base)


# Test the function
print(change_base(8, 3))  # Output: 22
print(change_base(8, 2))  # Output: 1000
print(change_base(7, 2))  # Output: 111
```
In this script, the `change_base` function recursively divides the input number `x` by the target base `base` until `x` is less than `base`. The remainder at each division step is prepended to a string, which is then returned as the result. This approach ensures that the digits are in the correct order for the target base. The script includes a check to ensure that the base is valid (between 2 and 9).