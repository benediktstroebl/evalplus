```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.

    Args:
        x (int): The number to be converted.
        base (int): The base to convert to.

    Returns:
        str: The string representation of the number in the given base.
    """
    convertString = "0123456789"
    if x < base:
        return convertString[x]
    else:
        return change_base(x // base, base) + convertString[x % base]


# Example usage
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This Python script uses recursion to convert a number from base 10 to any base less than 10. The `change_base` function takes an integer `x` and a base `base` as input, and returns a string representing `x` in the given base. It does this by recursively dividing `x` by the base and prepending the remainder to the result string. The `convertString` variable is used to map the remainders (0-9) to their corresponding digit characters.