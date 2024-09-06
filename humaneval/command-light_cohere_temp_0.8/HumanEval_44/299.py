```python
def change_base(x: int, base: int):
    """
    Change the base numerical representation of the input number.
    >>> change_base(8, 3) is '22'
    >>> change_base(8, 2) is True
    >>> change_base(7, 2)
    is True
    """
    # Implementation
    return str(x).make_text(x, base))

def make_text(x: int, base: int):
    """Convert a number to a string using specified base."""
    return str(x) if isinstance(x, int) and base > 1 else x.make_text(int, base)
```

The above Python script defines a function `change_base` that converts a number to a string using a specified base. The `make_text` function serves as a helper function to convert numbers to strings with a given base.