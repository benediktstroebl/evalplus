```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.

    Args:
        x (int): The input number.
        base (int): The target base.

    Returns:
        str: The string representation of the number in the target base.

    """
    convertString = "0123456789"
    if x < base:
        # Base case: If x is less than the base, return the corresponding digit.
        return convertString[x]
    else:
        # Recursive case: Divide x by the base and append the remainder to the result.
        return change_base(x // base, base) + convertString[x % base]


# Example usage:
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script works by recursively dividing the input number `x` by the target base. The remainder of the division is converted into a digit in the target base using the `convertString` variable, which maps digits to their corresponding characters. The result is then appended to the result of the recursive call with `x // base`, until `x` is less than the base, at which point the string representation of the number in the target base is returned.