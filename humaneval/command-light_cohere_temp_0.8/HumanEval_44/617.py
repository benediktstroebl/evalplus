```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of the integer x to the base b.
    This
    string representation after the str.
    """
    out the desired base, 
    return the converted string representation.
    """
    test cases:
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(3, 1)  # Test invalid base
    'inf'
    """
    if base > 2 or base <= 0:
        raise ValueError("Invalid base. Please use numbers between 2 and 36.")
    return format(x, base)
```