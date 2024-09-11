```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Parameters:
    x (int): Input number to be converted.
    base (int): Destination base for the conversion.
    
    Returns:
    str: String representation of the converted number.
    
    Examples:
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if x == 0:
        return '0'
    
    digits = "0123456789"
    result = ""
    
    while x:
        x, remainder = divmod(x, base)
        result = digits[remainder] + result
    
    return result

# Test the function
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines a function `change_base` that takes two integers as input: `x` and `base`. It converts the number `x` to the base specified by `base` and returns the result as a string. 

The function uses a while loop to perform the conversion. In each iteration, it uses the `divmod` function to divide `x` by `base` and calculate the remainder. The remainder is then used as an index into the string `digits` to get the corresponding digit in the new base. The digit is prepended to the result string. 

Finally, the function returns the result string. 

The script includes some test cases to demonstrate the function's behavior.