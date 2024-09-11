```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Args:
        x (int): The number to be converted.
        base (int): The target base (less than 10).
    Returns:
        str: String representation of the number after conversion.

    Examples:
        >>> change_base(8, 3)
        '22'
        >>> change_base(8, 2)
        '1000'
        >>> change_base(7, 2)
        '111'
    """
    result = ''
    while x > 0:
        result = str(x % base) + result
        x //= base
    return result

# Test the function
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines the `change_base` function and includes a docstring with a clear explanation of the function's purpose, parameters, and return value. It also includes example use cases and a section for testing the function. The function itself uses a simple iterative approach to perform the base conversion, continuously dividing the input number by the target base and appending the remainder to the result string.