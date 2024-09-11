```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Parameters:
    x (int): The number to be converted.
    base (int): The base to convert to.
    
    Returns:
    str: The string representation of x in base.
    """
    digits = "0123456789"
    if base >= 10:
        raise ValueError("Base numbers are less than 10")
    
    result = ""
    while x > 0:
        result = digits[x % base] + result
        x = x // base
    return result


# Test cases
print(change_base(8, 3))   # '22'
print(change_base(8, 2))   # '1000'
print(change_base(7, 2))   # '111'
```

This Python script defines a function `change_base` to convert a number from base 10 to any base less than 10. It uses the modulo operator (`%`) and integer division (`//`) to calculate the remainder and quotient of the number `x` divided by the base `base`. The remainder is used to determine the next digit in the result, and the quotient is used to repeat the process until `x` is 0. The result is a string representation of the number in the specified base.