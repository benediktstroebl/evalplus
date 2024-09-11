```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.

    Args:
    x (int): The number to convert.
    base (int): The target numerical base (2-9).

    Returns:
    str: The string representation of x in the target base.

    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if not 2 <= base <= 9:
        raise ValueError("Base must be between 2 and 9")
    
    if x == 0:
        return '0'

    digits = []
    while x:
        digits.append(int(x % base))
        x //= base

    return ''.join(map(str, digits[::-1]))

# Test cases
print(change_base(8, 3))  # Output: 22
print(change_base(8, 2))  # Output: 1000
print(change_base(7, 2))  # Output: 111
```
This script defines a function `change_base` that takes an integer `x` and a base `b` as input, and returns the string representation of `x` in the target base `b`. It uses the standard algorithm for base conversion: repeatedly divide the number by the base and record the remainders. The base is chosen to be at least 2 and at most 9. The function also handles the case where the input number is 0.