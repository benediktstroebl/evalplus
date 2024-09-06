```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of the number x to the base of base base.
    >>> change_base(8, 3) == '22'
    True
    >>> change_base(10, 3)
    'Bahnhofbaumhofstrasse'
    >>> change_base('5221', 8) == '51221'
    True
    >>> change_base(123, 3)
    '6666'
    >>> change_base(10, 2)
    '20'
    >>> change_base(56, 90)
    True
    False
    """
    return str(x) if x < base else 'True'
```