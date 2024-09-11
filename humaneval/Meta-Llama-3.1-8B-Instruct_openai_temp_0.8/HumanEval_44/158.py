```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.

    Args:
        x (int): The number to be converted.
        base (int): The target base.

    Returns:
        str: The string representation of x in base.

    Raises:
        ValueError: If base is not less than 10.
    """
    if base < 2 or base > 10:
        raise ValueError("Base must be between 2 and 10")

    if x == 0:
        return '0'

    nums = "0123456789"
    result = ""

    while x > 0:
        result = nums[x % base] + result
        x //= base

    return result

# Test cases
print(change_base(8, 3))  # Output: 22
print(change_base(8, 2))  # Output: 1000
print(change_base(7, 2))  # Output: 111
try:
    print(change_base(10, 11))
except ValueError as e:
    print(e)  # Output: Base must be between 2 and 10
```
This Python script defines a function `change_base` that changes the base of an integer. It first checks if the base is between 2 and 10. Then, it converts the number to the target base by repeatedly taking the remainder of the number with the base and appending the corresponding digit to the result. The number is then divided by the base and the remainder is used as the next digit. This process continues until the number becomes zero. The function returns the string representation of the number in the target base. If the base is not within the valid range, it raises a `ValueError`.