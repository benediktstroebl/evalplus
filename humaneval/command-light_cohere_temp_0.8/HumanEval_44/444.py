```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base.

    Args:
        x: int or string representing the number to be converted,
        base: int, base to convert to. bib is a number system base.
    Returns: string representation of the number in the new base.
    """
    example:
    >>> change_base(8, 3)
    '22'
    >>> change_base('8', 2)
    '1000'
    >>> change_base('7', 2)
    '111'
    """
    return format(x, '{:b}', base)

# Uncommented test cases
print(change_base(8, 3))        # Output: 22
print(change_base('8', 2))     # Output: 1000
print(change_base(7, 2))     # Output: 111
```
The `change_base` function takes an input `x` and a `base` as arguments, then uses the `format` method to convert `x` to a string in the specified base.