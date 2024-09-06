```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of the input number x to base base.
    If numbers that do not fit the base will get truncated or wrap around.
    """ example:
    >>> change_base(1234567, 8)
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(None, int)
    >>> change_base(12, 2) # wrap around
    '122'
    >>> change_base(12, 0) # return zero in base 0
    '0'
    >>> change_base('48', 4) # wrap around
    '48'
    >>> change_base('48', 5) # return as is
    '48'
    """
    if base < 2 or base > 36:
        raise TypeError("base must be between 2 and 36")
        
    return f"{x:0>{base}}"
```