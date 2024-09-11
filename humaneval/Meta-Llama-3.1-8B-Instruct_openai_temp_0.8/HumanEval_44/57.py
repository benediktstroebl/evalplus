```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    :param x: Input integer number
    :param base: Target base for the conversion (less than 10)
    :return: String representation of the converted number
    """
    if not isinstance(x, int) or not isinstance(base, int):
        raise ValueError("Input must be integers")
    if not 2 <= base < 10:
        raise ValueError("Base must be between 2 and 9 (inclusive)")
    
    if x == 0:
        return '0'
    
    digits = []
    while x:
        digits.append(int(x % base))
        x //= base
    
    return ''.join(map(str, digits[::-1]))


# Test the function
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This Python script defines a function `change_base` that converts an integer `x` to a different base `base` (between 2 and 9). The function uses a simple iterative approach, continuously dividing the input number by the target base and appending the remainder to the result as a digit. The result is then returned as a string in the specified base. If the input number is 0, the function returns '0'. The script includes input validation to ensure that the inputs are integers and the base is between 2 and 9.