```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    :param x: The number to convert.
    :param base: The base to convert to.
    :return: A string representation of the converted number.
    """
    if x == 0:
        return '0'
    
    result = ''
    while x > 0:
        x, remainder = divmod(x, base)
        result = str(remainder) + result
    
    return result

# Test the function
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines a function `change_base` that takes an integer `x` and a base `base` as input. It then converts the number `x` to the base `base` and returns the result as a string. The function uses a while loop to repeatedly divide the number by the base and append the remainder to the result string. If the input number is 0, it immediately returns '0'.