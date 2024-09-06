```python
def change_base(x: int, base: int):
    """
    Change the base of input number x to base base.
    :return string representation after conversion
    """
    base numbers less than 2 or non-integer bases are invalid
    """
    assert isinstance(base, int) and base > 0, "Invalid base number"
    return format(x, base)
```