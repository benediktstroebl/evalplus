```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of the integer x to the base b.
    >>> change_base(8, 3)  # Should return '22'
    >>> change_base(8, 2)  # Should return '1000'
    >>> change_base(7, 2)  # Should return '111'
    """
    # Following is implementation of the above function
    if base == 10:
        return str(x)
    else:
        return format(x, str(base))
```