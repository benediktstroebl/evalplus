```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.
    
    Parameters:
    x (int): The number to convert.
    base (int): The base to convert to.
    
    Returns:
    str: The string representation of x in base base.
    """
    if not isinstance(x, int) or not isinstance(base, int):
        raise TypeError("Input must be integers")
    if base < 2 or base > 9:
        raise ValueError("Base must be between 2 and 9")
    
    digits = "0123456789"
    if x < base:
        return digits[x]
    else:
        return change_base(x // base, base) + digits[x % base]

# Test the function
print(change_base(8, 3))  # Output: 22
print(change_base(8, 2))  # Output: 1000
print(change_base(7, 2))  # Output: 111
```

This script defines a function `change_base` that converts a given integer `x` to a specified base. It uses recursion to achieve this by repeatedly dividing the number by the base and appending the remainder to the result. The remainders are converted to their corresponding digits (0-9) using a string of digits. If the base is invalid (less than 2 or greater than 9), a ValueError is raised. If the inputs are not integers, a TypeError is raised.