```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number x to base base.
    We use thelogger notation for the result
    """
    if x < 0 or base < 2:
        raise ValueError("Base must be 2 or 10, and x must be positive.")
    elif base == 10:
        return str(x)
    else:
        return "{0" * x}
```