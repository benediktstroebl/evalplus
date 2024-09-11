```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.

    Parameters:
    x (int): The number to be converted.
    base (int): The base to which the number will be converted.

    Returns:
    str: The string representation of the number after conversion.
    """
    convertString = "0123456789ABCDEF"
    if x < base:
        return convertString[x]
    else:
        return change_base(x // base, base) + convertString[x % base]


# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This Python script defines a recursive function `change_base` to convert a number `x` from base 10 to a different base `base`. The function uses a string `convertString` to map the digits of the new base to their corresponding characters. The function recursively divides the number by the base until the quotient is less than the base, then constructs the string representation of the number by appending the remainder to the string representation of the quotient.