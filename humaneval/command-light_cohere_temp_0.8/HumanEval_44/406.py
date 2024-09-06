```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of integer x to base b.
    :param:
        x: int,
        Number to be converted
        base: int,
                Base to which convert
    :return: string representation of x in base b
    """
    if base < 2 or base > 36:
        raise ValueError("Invalid base number")
    # convert number to string in base 'b'
    return format(x, base)
```