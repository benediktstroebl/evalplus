```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.

    Args:
        x (int): Input number to be converted.
        base (int): Target base for conversion.

    Returns:
        str: String representation of the number in the target base.
    """
    if base < 2 or base >= 10:
        raise ValueError("Base numbers should be less than 10")

    digits = []
    while x:
        digits.append(int(x % base))
        x //= base

    return ''.join(map(str, digits[::-1]))

# Example usage:
print(change_base(8, 3))  # Output: 22
print(change_base(8, 2))  # Output: 1000
print(change_base(7, 2))  # Output: 111
```

This script defines the `change_base` function which converts a base-10 integer to any base between 2 and 9. It uses a while loop to continuously divide the input number by the target base and append the remainder to a list. Finally, it reverses the list and joins the digits into a string. The example usage at the end shows how to use the function with the given test cases.