```python
def change_base(x: int, base: int) -> str:
    """Change the base of input number x to base base.
    >>> change_base(8, 3) == '22'
    True
    >>> change_base(8, 2) == '1000'
    True
    >>> change_base(7, 2) == '111'
    True
    >>> change_base(7, 10)
    Fails
    """
    if base > x:
        raise ValueError("Base number must be less than or equal to input number.")
    return format(x, base)
```