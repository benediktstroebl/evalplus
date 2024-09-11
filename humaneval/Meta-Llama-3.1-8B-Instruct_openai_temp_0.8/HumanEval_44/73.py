```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Args:
        x (int): The number to be converted.
        base (int): The base to convert the number to.

    Returns:
        str: String representation of the number in the new base.
    """
    if base < 2 or base > 10:
        raise ValueError("Base must be between 2 and 10.")
    
    convertString = "0123456789"
    result = ""
    
    while x > 0:
        result = convertString[x % base] + result
        x = x // base
    
    return result


# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines a function `change_base` that converts an integer `x` to a string representation in a given base. It uses a while loop to continuously divide the input number by the base and append the remainder to the result string. The remainders are mapped to their corresponding digits in the new base using the `convertString` variable. The function raises a `ValueError` if the base is not between 2 and 10. Finally, the script includes test cases to demonstrate the function's correctness.