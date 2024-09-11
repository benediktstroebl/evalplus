### Change Numerical Base of a Number
#### Problem Statement
Convert a given number `x` to a different base `base`.

#### Solution
```python
def change_base(x: int, base: int) -> str:
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.
    
    Args:
    x (int): The input number to be converted.
    base (int): The target base for the conversion.
    
    Returns:
    str: The string representation of the converted number.
    
    Example:
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """

    convertString = "0123456789"
    result = ""

    while x > 0:
        # Extract the remainder of the number when divided by the base
        remainder = x % base
        result = convertString[remainder] + result
        x = x // base

    return result

# Testing the function
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```
This Python script defines a function `change_base(x, base)` that converts the input number `x` to the desired base `base`. It uses a while loop to extract the remainder of the number when divided by the base, and prepends the corresponding digit from the `convertString` to the result string. The process continues until the number becomes 0, at which point the result string is returned.