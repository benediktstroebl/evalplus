```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of the integer 'x' to base 'base'.
    Return the string representation after conversion.
    """
    example usage: >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    return hex(x)[2:].zfill()[base-1] + str(x)[-::-1]
```