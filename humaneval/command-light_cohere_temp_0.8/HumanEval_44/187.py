```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another. specific base.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(10, 10)
    '10000000000'
    >>> change_base(10, 'a')
    Traceback (most recent call last):
      File "<string>", line 7:10
        TypeError: unsupported operand type(10, 'a') for multiplication on
    >>> change_base(-100, 'a')
    Traceback (most recent call last):
      File "<string>", line 7:10
        TypeError: unsupported operand type(-100, 'a') for multiplication on
    """
    if x < 0 or base < 0 or base < x:
        raise ValueError("input or base is negative")
    if base == x == 0:
        return str(x)
    res = str(x, base)
    return res
```