### Change Numerical Base
```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.

    Args:
    x (int): The number to be converted.
    base (int): The target base (less than 10).

    Returns:
    str: The converted number in string format.
    """
    if not isinstance(x, int) or not isinstance(base, int):
        raise TypeError("Both x and base must be integers.")
    if base < 2 or base >= 10:
        raise ValueError("Base must be between 2 and 9.")
    if x == 0:
        return '0'

    digits = []
    while x:
        digits.append(int(x % base))
        x //= base
    return ''.join(map(str, digits[::-1]))

# Example usage:
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```
This script uses a simple iterative approach to convert a number from base 10 to any base between 2 and 9. The function `change_base` takes two arguments: `x` (the number to be converted) and `base` (the target base). It returns the converted number as a string. If `x` or `base` is not an integer, or if `base` is out of range, the function raises an error.