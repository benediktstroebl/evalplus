Here's the code:
```python
def change_base(x: int, base: int):
    """
    Convert a number to a string representation using a specified base.
    Args:
        x: int, the number to convert
        base: int, the base to use (e.i string representation will the main number in base 10 is 10)
    Returns:
        str
    """
    return str(x) if x < base else str(x, base)
```
This code provides a function `change_base` that converts a given number `x` to a string representation using a specified base. It uses the `str` to check whether `x` is less than `base` and, if so, converts `x` to its string representation in base 10. Otherwise, it converts `x` to the desired base.