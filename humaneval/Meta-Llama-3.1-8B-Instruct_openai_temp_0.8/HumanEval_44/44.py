```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    :param x: input number
    :param base: target base
    :return: string representation of number in base base
    """
    if x == 0:
        return '0'
    
    digits = []
    while x:
        digits.append(int(x % base))
        x //= base
    
    return ''.join(map(str, digits[::-1]))

# Test cases
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

This script defines a function `change_base` that converts an integer `x` to a specified base `base` (less than 10). The conversion is done by repeatedly taking the remainder of the integer when divided by the base and appending it to the result. The integer is then divided by the base, and this process is repeated until the integer is 0. The result is then returned as a string.

The test cases at the end of the script demonstrate the function's behavior for the provided examples.