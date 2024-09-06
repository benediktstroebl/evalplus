```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of input number x to base base.
    >>> change_base(8, 3) == '22'
    True
    >>> change_base(8, 2) == '1000'
    True
    >>> change_base(7, 2) == '111'
    True
    """
    if x < 0 or base < 0 or base < x:
        raise ValueError("Invalid arguments. The base cannot be less than 0 and the number cannot be negative.")
    return format(x, f"{base}-"[:-len(str(x))])
```