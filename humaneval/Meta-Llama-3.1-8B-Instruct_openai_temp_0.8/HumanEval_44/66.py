```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.

    Parameters:
    x (int): The number to be converted.
    base (int): The target base of the number. (Base numbers are less than 10)

    Returns:
    str: The string representation of x in base.
    """
    if x == 0:
        return '0'

    digits = []
    while x:
        x, remainder = divmod(x, base)
        digits.append(str(remainder))
    return ''.join(reversed(digits))

# Test cases
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

This script defines the `change_base` function, which takes an integer `x` and a base `base` as input and returns a string representation of `x` in base `base`. It uses a while loop to perform the conversion. The `divmod` function is used to get both the quotient and the remainder of the division of `x` by `base` in each iteration. The remainder is converted to a string and appended to the list of digits. Finally, the digits are reversed and joined together into a string. The test cases at the end demonstrate the function's correctness.