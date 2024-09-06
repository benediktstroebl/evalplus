```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base.

    :paramaters:
        x: int, The number to be changed
        base: int, The base to which the number will be changed.

    :return: str, The number converted to a string in the desired base.
    """
    test cases:
    >>> change_base(8, 3)
    '22'
    >>> change_base(123, 4)
    '0123456789'
    >>> change_base(56, 8)
    '5 606 570'
    >>> change_base(123, 2)
    '1000000'
    """
    return format(x, f"{base}")
```