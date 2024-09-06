```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another.
    :param x: int, base: int
    :return: string representation after conversion
    """
    if base < 2 or base > 36:
        raise ValueError("Invalid base number")
    return format(x, base)
```