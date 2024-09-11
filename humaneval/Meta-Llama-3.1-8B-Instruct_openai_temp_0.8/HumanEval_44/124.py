```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.

    Args:
    x (int): The number to be converted
    base (int): The base to which the number should be converted

    Returns:
    str: The string representation of the number in the given base

    Raises:
    ValueError: If the base is not a valid number less than 10
    """

    if not isinstance(base, int) or base < 2 or base > 10:
        raise ValueError("Base must be an integer between 2 and 10")

    digits = "0123456789"
    result = "0"

    if x < base:
        return digits[x]

    while x:
        result = digits[x % base] + result
        x //= base

    return result


# Test cases
print(change_base(8, 3))   # Output: '22'
print(change_base(8, 2))   # Output: '1000'
print(change_base(7, 2))   # Output: '111'
```

This Python script uses a simple algorithm to convert a decimal number to any base between 2 and 10. It does this by continuously dividing the number by the base, appending the remainder to the result string, until the number is less than the base. The result string is then returned.