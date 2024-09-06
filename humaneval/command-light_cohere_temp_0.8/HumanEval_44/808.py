```python
def change_base(x: int, base: int) -> str:
    """
    Convert input number x to a string representation in the specified base.
    The base can be 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(0, 10)
    '0'
    >>> change_base(1, 10)
    '1'
    >>> change_base('12', 10)
    '1200'
    >>> change_base(123, 5)
    '2(...)'
    >>> change_base(123456, 7)
    '123456'
    """
    # Perform base conversion using reverse operation of builtin int(x, base)
    return str(int(x, base))
```