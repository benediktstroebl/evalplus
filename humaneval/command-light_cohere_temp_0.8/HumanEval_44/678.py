```python
def change_base(x: int, base: int):
    """
    Change the base of integer x to base base, 
    without returning a string representation.
    >>> change_base(8, 3)  # return '22'
    >>> change_base(8, 2)  # return '1000'
    >>> change_base(7, 2)  # return '111'
    """
    return hex(x)[2:].zfill()
```