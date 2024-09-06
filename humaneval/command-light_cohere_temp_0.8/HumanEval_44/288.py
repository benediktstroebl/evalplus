```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    return string representation after conversion.
    base numbers less 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(10, 10)
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(10) for +() with base_or_number (int)
    """
    base_or_number = 10  # Assuming 10 as base or number
    return f"{base_or_number}{x}"
```