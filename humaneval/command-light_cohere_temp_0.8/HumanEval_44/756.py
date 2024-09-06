```python
def change_base(x: int, base: int):
    """
    Change the base of a number x to base b.
    >>> change_base(8, 3) == '22'
    True
    >>> change_base(8, 2) == '1000'
    True
    >>> change_base(7, 2) == '111'
    True
    >>> change_base(0, 1)
    Traceback (most recent call last):
      File "<stdin>", line 4, in <module>
    AssertionError: 0 not equal to any integer
    """
    if base <= 0 or base > 2:**
        raise ValueError("Base number should be between 1 and 2.")
    return format(x, base)
```