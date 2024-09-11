```markdown
**Change Numerical Base**
=========================

This script converts a given number from decimal to any base between 2 and 9.

**Code**
------

```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.

    Args:
    x (int): The number to be converted.
    base (int): The target base.

    Returns:
    str: The string representation of the number in the target base.

    Examples:
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if not isinstance(x, int) or not isinstance(base, int):
        raise TypeError("Both x and base must be integers.")
    if base < 2 or base > 9:
        raise ValueError("Base must be between 2 and 9.")
    if x == 0:
        return '0'

    digits = []
    while x:
        digits.append(int(x % base))
        x //= base

    return ''.join(map(str, digits[::-1]))

# Example usage
print(change_base(8, 3))  # Outputs: '22'
print(change_base(8, 2))  # Outputs: '1000'
print(change_base(7, 2))  # Outputs: '111'
```

**Explanation**
--------------

The `change_base` function takes two arguments: `x` (the number to be converted) and `base` (the target base). It first checks if both `x` and `base` are integers and if `base` is within the valid range (2-9). If not, it raises a `TypeError` or `ValueError` respectively.

It then enters a while loop that continues until `x` is 0. In each iteration, it calculates the remainder of `x` divided by `base` (which is the next digit in the target base) and appends it to the `digits` list. It then performs integer division of `x` by `base` to remove the last digit.

After the loop, it reverses the `digits` list (since we appended the digits in reverse order) and joins them into a string using the `join` function. The resulting string is the representation of the number in the target base.