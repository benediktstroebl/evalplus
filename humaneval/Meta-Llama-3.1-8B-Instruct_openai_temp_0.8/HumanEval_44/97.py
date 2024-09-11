```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.
    
    Parameters:
    x (int): The number to be converted.
    base (int): The base to convert to.
    
    Returns:
    str: String representation of x in the specified base.
    """
    convertString = "0123456789"
    result = ""

    while x > 0:
        result = convertString[x % base] + result
        x = x // base

    return result

# Test the function
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines a function `change_base` that takes an integer `x` and a base `base` as input, and returns a string representation of `x` in the specified base. The function uses the modulo operator (`%`) to get the remainder of `x` divided by `base`, and the floor division operator (`//`) to get the quotient of `x` divided by `base`. This process is repeated until `x` is 0, at which point the result is in the desired base. The `convertString` variable is a string that maps the numbers 0-9 to their corresponding digits in the new base.