```markdown
### Change Numerical Base

This script defines a function `change_base` that converts a given number `x` to a new base.

#### Code

```python
def change_base(x: int, base: int) -> str:
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.

    Args:
        x (int): The number to be converted.
        base (int): The target base.

    Returns:
        str: The string representation of x in the target base.
    """
    if x < base:
        return str(x)
    else:
        return change_base(x // base, base) + str(x % base)


# Example usage:
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

#### Explanation

This function uses a recursive approach to perform the conversion. If the input number `x` is less than the target base, it simply returns the number as a string. Otherwise, it recursively calls itself with `x` divided by the base and the remainder as the new `x`, then appends the remainder to the result.

The `//` operator is used for integer division, which discards the remainder and returns the quotient. The `%` operator is used to get the remainder of the division.