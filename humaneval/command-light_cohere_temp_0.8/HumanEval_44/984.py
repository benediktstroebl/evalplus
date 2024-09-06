```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of the given number to base 'base'.

    Args:
        x (int): The number to be converted.
        base (int): The base to which the number will be converted.

    Returns: string representation of the converted number.
    """
    base numbers are 10 or can be converted to other base numbers.

    Example following the example:
    >>> change_base(8, 3)  # Result: '22'
    >>> change_base(8, 2)  # Result: '1000'
    >>> change_base(7, 2)  # Result: '111'
    """
    return format(x, f', base)
```