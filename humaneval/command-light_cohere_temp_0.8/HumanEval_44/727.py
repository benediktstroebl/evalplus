Here's the solution:
```python
def change_base(x: int, base: int) -> str:
    """
    Convert number to a string using given base.
    >>> change_base(8, 3) == '22'
    >>> change_base(8, 2) == '1000'
    >>> change_base(7, 2) == '111'
    True
    """
    # Convert to string using decimal number representation
    return format(x, f"{base}")
```