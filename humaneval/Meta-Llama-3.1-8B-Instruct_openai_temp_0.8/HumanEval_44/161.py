```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Args:
    x (int): The number to be converted.
    base (int): The target base.

    Returns:
    str: A string representation of the number in the target base.
    """
    convertString = "0123456789"
    if x < base:
        return convertString[x]
    else:
        return change_base(x // base, base) + convertString[x % base]


# Test the function
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines a function `change_base` that takes an integer `x` and a base `base` as input and returns a string representation of `x` in the target base. It uses recursion to perform the conversion, and the `convertString` variable is used to map the digits 0-9 to their corresponding characters. The script also includes test cases to demonstrate the function's correctness.