```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Parameters:
    x (int): The number to be converted.
    base (int): The base to which the number should be converted.
    
    Returns:
    str: The string representation of the number in the new base.
    """
    convertString = "0123456789"
    result = ""

    while x > 0:
        result = convertString[x % base] + result
        x = x // base

    return result

# Test cases
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

This script defines a function `change_base` that converts a given integer `x` to a specified base `base`. It uses a while loop to repeatedly divide the input number by the base and append the remainder to the result string, effectively converting the number to the desired base. The script then includes test cases to demonstrate the function's correctness.