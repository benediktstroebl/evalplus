```python
def change_base(x: int, base: int):
    """
    Changes the base of the input number x to base base, and returns the string representation.
    >>> change_base(8, 3) == '22'
    >>> change_base(8, 2) == '1000'
    >>> change_base(7, 2) == '111'
    """
    return chr(97 + x * (ord(base) - 97))
```