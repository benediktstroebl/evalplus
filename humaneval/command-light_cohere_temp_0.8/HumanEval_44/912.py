```python
def change_base(x: int, base: int) -> str:
    """
    Changes the base of a number to another base.
    Returns a str string representation of the number after the base change.
    """
    example:
    >>> change_base(8, 3)
    '22'
    >>> change_base(10, 2) # bases up from 10
    '100'
    >>> change_base(111, 5) # base is 5
    '1111'
    """
    return "{:>".format(x, base)
```