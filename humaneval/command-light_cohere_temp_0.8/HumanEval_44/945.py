```python
def change_base(x: int, base: int):
    """
    Change the base of a number to another base.
    >>> change_base(8, 3) == '22'
    >>> change_base(8, 2) == '1000'
    >>> change_base(7, 2) == '111'
    False
    """
    if base > x or base < 2 or base <= 0:
        raise ValueError("Base number should be > 0 and < than x")
    new_str = str(x)
    while True:
        dig = str(x % base)
        if dig == dig[::-1]:
            break
        new_str = new_str.format(dig, new_str)
    return new_str
```