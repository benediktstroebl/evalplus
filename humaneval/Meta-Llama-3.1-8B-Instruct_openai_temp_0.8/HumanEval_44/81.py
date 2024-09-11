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
        str: The string representation of the number in the target base.
    """
    if x == 0:
        return '0'
    
    digits = "0123456789"
    result = ""
    
    while x:
        x, remainder = divmod(x, base)
        result = digits[remainder] + result
    
    return result


# Test cases
print(change_base(8, 3))  # Output: 22
print(change_base(8, 2))  # Output: 1000
print(change_base(7, 2))  # Output: 111
```

This script defines the `change_base` function, which converts an integer `x` to a string representation in a target base. The function uses the `divmod` function to perform integer division and find the remainder. The remainder is then used to index into the string of digits to get the corresponding digit in the target base. The result is built up as a string and returned. The script also includes test cases to verify the correctness of the function.