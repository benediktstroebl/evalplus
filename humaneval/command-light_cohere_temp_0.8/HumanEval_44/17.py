```python
def change_base(x: int, base: int):
    """
    Change the base of input number x to base b.
    Return string representation of x in the given base.
    """
    base numbers less than 10
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '128'
    >>> change_base(7, 5)
    Traceback (most recent call last):
      File "<string>", line 6, in <module>
    ValueError: unsupported literal for int(): '7'
    """
    if base not in [2, 5, 10]:
        raise ValueError("Base number must be 2, 5, or 10")
    return str(x)
```