```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of integer number x to base base.
    return string representation after conversion.
    base numbers arens between 2 and 36.
    """
    numbers less than 10.
    >>> change_base(123, 45)
    '2345'
    >>> change_base(123, 97)
    TraceError: incompatible argument types(<int128>, 45)
    """
    if base > 36 or base < 2:
        raise ValueError("base must be between 2 and 36")
    return format(x, f"{base}"), base
```