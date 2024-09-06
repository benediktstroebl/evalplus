```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    return string representation after conversion.
    base numbers less 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(5, 3)
    Traceback (most recent call last):
    ...
    ValueError: base must be less than or equal to 2 and greater than 0
```
This code defines a function `change_base` that takes two arguments: `x` (the number to be converted) and `base` (the base to which the number will be converted). The function converts `x` to a string representation using the specified base, and returns the result.