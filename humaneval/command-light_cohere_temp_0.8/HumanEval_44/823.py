```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base base.
    """
    return string representation using base conversion.
    """
    Python example:
    >>> change_base(8, 3)  # Output: '22'
    >>> change_base(8, 2)  # Output: '1000'
    >>> change_base(7, 2)  # Output: '111'
    """
    return '{:0{}d}'.format(x, base)
```