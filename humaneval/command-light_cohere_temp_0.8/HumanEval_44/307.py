```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of integer x to base base.
    Convert x to as string using base
    >>> change_base(8, 3)
    '22'
    >>> change_base(5, 10)
    '50'
    >>> change_base(35, 10)
    '35000'
    >>> change_base(12, 2)
    '12'
    >>> change_base(93, 22)
    '49'
    >>> change_base(170, 56)
    '11111'
    """
    assert isinstance(x, int) and x > 0, "Input must be a positive integer"
    assert isinstance(base, int) and base > 0 and base <= 36, "Base must be a positive integer less than 37"
    return '{:b}'.format(x, base)
```
The function takes two arguments: x, which is the number to be converted, and base, which is the desired base for the conversion. The function uses the Python's built-in `{:b}`.format method to convert the number to a string representation using the specified base.