```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.

    Args:
        x (int): Number to convert
        base (int): Desired base

    Returns:
        str: String representation of number in desired base
    """
    if x == 0:
        return '0'
    digits = []
    while x:
        digits.append(int(x % base))
        x //= base
    return ''.join(map(str, digits[::-1]))

print(change_base(8, 3))  # Output: 22
print(change_base(8, 2))  # Output: 1000
print(change_base(7, 2))  # Output: 111
```

In this script, the function `change_base` takes an integer `x` and a base `base` as input, and returns the string representation of `x` in the given base. It handles the conversion by repeatedly dividing `x` by `base` and appending the remainder to the result. The result is then reversed and converted to a string before being returned. The script also includes a base case for when `x` is 0, in which case it returns '0' directly. The script then prints out the results of the function for the provided test cases.