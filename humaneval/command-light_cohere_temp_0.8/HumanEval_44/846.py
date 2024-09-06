```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number x to base b.
    >>> change_base(123, 3)  # return '22'
    >>> change_base(35, 5) # return '005'
    >>> change_base(8, 7)  # raise error
    'inf'

    When x or base is less than 0 or non-integer, return 'inf'.
    """
    if x < 0 or not isinstance(x, int):
        return 'inf'
    if base < 2 or not isinstance(base, int):
        return 'inf'
    return '{:0bX}'.format(x, base)
```