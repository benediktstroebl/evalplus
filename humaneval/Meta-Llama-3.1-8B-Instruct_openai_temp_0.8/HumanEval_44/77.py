```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.

    Parameters:
    x (int): The number to be converted.
    base (int): The target base.

    Returns:
    str: The string representation of x in base base.
    """
    convertString = "0123456789"
    result = ""
    
    while x > 0:
        result = convertString[x % base] + result
        x = x // base
    
    return result

# Test cases
print(change_base(8, 3))  # Expected output: '22'
print(change_base(8, 2))  # Expected output: '1000'
print(change_base(7, 2))  # Expected output: '111'
```

In this script, the `change_base` function uses a simple approach to convert a base-10 integer `x` to a different base `base`. It repeatedly uses the modulo operator (`%`) to extract the remainder of `x` divided by the target base, and then uses integer division (`//`) to update `x` to its quotient. The remainder is then converted to its corresponding digit character from the `convertString` and prepended to the result. This process is repeated until `x` is reduced to 0. The final result is the string representation of `x` in base `base`.