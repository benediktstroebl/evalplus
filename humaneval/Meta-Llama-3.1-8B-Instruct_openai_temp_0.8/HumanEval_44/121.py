### Change Numerical Base of a Number
```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.

    Parameters:
    x (int): The number to be converted.
    base (int): The base to convert the number to.

    Returns:
    str: The string representation of the number in the new base.
    """
    if x < 0:
        sign = -1
        x = -x
    else:
        sign = 1

    convertString = "0123456789ABCDEF"
    result = ""

    while x > 0:
        result = convertString[x % base] + result
        x = x // base

    return (-1) ** sign * result


# Test cases
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```
This script defines a function `change_base` that takes an integer `x` and a base as input and returns a string representing the number `x` in the given base. It handles negative numbers by storing the sign separately and performing the conversion on the absolute value. The conversion is done by repeatedly taking the remainder of `x` divided by the base (which gives the last digit in the new base) and appending it to the result string. The quotient of `x` divided by the base is then used as the new `x` in the next iteration until `x` becomes 0.