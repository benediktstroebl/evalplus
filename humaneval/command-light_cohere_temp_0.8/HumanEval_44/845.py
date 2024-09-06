```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of a number to another base.
    Base numbers less than 10.
    >>> change_base(8, 3) == '22'
    True
    >>> change_base(8, 2) == '1000'
    True
    >>> change_base(7, 2) == '111'
    True
    """
    # Perform the base conversion
    return format(x, f"{base}", max_digits=20)
```