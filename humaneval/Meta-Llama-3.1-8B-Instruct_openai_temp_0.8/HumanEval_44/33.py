```python
def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.

    :param x: The number to convert.
    :param base: The target numerical base.
    :return: The string representation of x in base.
    """
    if x == 0:
        return '0'
    
    digits = []
    while x:
        digits.append(int(x % base))
        x //= base
    
    # Reverse the list of digits
    digits.reverse()
    
    # Convert the digits to a string
    return ''.join(str(digit) for digit in digits)


# Test cases
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

This script defines a function `change_base` that takes an integer `x` and a base `base` as input and returns the string representation of `x` in base `base`. The function uses a while loop to repeatedly divide `x` by `base` and append the remainder to the list of digits. After the loop, the list of digits is reversed and converted to a string using the `join` function. The function also includes a special case for `x == 0`, in which case it immediately returns '0'. The script includes the same test cases as the original problem statement.