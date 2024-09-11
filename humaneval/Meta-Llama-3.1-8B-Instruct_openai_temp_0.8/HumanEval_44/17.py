```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.

    Parameters:
    x (int): The input number to be converted.
    base (int): The target base.

    Returns:
    str: The string representation of the number x in the base base.
    """
    if x == 0:
        return '0'

    digits = '0123456789'
    result = ''

    while x:
        result = digits[x % base] + result
        x = x // base

    return result

# Example usage:
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script works by continuously dividing the number x by the target base, appending the remainder to the result, and updating x to the quotient of the division. The remainders are converted to their corresponding digits in the target base by looking them up in the `digits` string. This process continues until x is reduced to 0, at which point the conversion is complete. The final result is returned as a string.