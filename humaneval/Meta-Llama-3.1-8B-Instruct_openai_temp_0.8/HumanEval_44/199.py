### Change Numerical Base of a Number
Here's a Python function that converts a number from one base to another within the range of base < 10.
```python
def decimal_to_base(x: int, base: int) -> str:
    """
    Convert a decimal number to any base between 2 and 9.

    Args:
        x (int): The decimal number to convert.
        base (int): The base to convert to.

    Returns:
        str: The representation of x in base.
    """
    if not isinstance(x, int) or not isinstance(base, int):
        raise TypeError("Both x and base must be integers.")
    if base < 2 or base > 9:
        raise ValueError("Base must be between 2 and 9.")
    if x == 0:
        return '0'

    digits = ""
    while x:
        digits = str(x % base) + digits
        x //= base

    return digits


def change_base(x: int, base: int) -> str:
    """
    Change numerical base of input number x to base.

    Args:
        x (int): The number to convert.
        base (int): The base to convert to.

    Returns:
        str: The representation of x in base.
    """
    return decimal_to_base(x, base)


# Example use cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```
This script defines two functions: `decimal_to_base` and `change_base`. The `decimal_to_base` function takes a decimal number and a base as input and returns the representation of the number in the given base. The `change_base` function is a wrapper around `decimal_to_base` with the same functionality.

Both functions handle errors for invalid input, ensuring that the base is between 2 and 9 and that both the input number and base are integers. If the input number is 0, it returns '0'. Otherwise, it divides the number by the base and appends the remainder to the digits string until the number becomes 0. The digits are then reversed to form the final representation.