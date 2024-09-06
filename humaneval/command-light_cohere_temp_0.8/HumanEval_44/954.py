```python
def change_base(x: int, base: int):
    """
    Change the base of the input number x to base b.
    Return string representation after conversion.
    base numbers less 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(1, 3)
    Tracearith error: unable integer instantiation: '1'
    """
    if base > x:
        raise ValueError("base must be less than or equal to input number")
    return str(x)
```