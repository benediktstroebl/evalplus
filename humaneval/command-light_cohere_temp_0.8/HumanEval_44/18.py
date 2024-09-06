```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base base.
    Return string representation.
    base numbers 10.
    >>> change__base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if x < 0 or base < 2:
        raise ValueError("Invalid input. Base should be between 2 and 10.")
    return format(x, f"{base}", "l")
```