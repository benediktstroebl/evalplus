Here is a Python script that solves the problem:
```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if base < 2 or base > 9:
        raise ValueError("Base must be between 2 and 9")
    if x == 0:
        return '0'
    result = ''
    while x:
        x, remainder = divmod(x, base)
        result = str(remainder) + result
    return result

# Test cases
print(change_base(8, 3))  # Output: 22
print(change_base(8, 2))  # Output: 1000
print(change_base(7, 2))  # Output: 111
```
This script defines a function `change_base` that takes an integer `x` and a base `base` as input, and returns the string representation of `x` in base `base`. The function uses a while loop to repeatedly divide `x` by `base` and append the remainder to the result string. If `base` is not between 2 and 9, the function raises a `ValueError`. Finally, the script includes some test cases to verify the correctness of the function.