```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    Return string representation after conversion.
    base numbers less 10
    common base.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '100'
    >>> change_base(7, 2)
    '111'
    >>> change_base(10, 5)
    '001'
    >>> change_base('abc123', 1)
    Traceback (most recent call last):
      ...
    ValueError: invalid literal for int() with base 10
```
The function `change_base` takes two arguments: `x`, which is the number to be converted, and `base`, which is the desired base to which the number will be converted. The function uses the specific base numbers to perform the conversion, ensuring that the result is a valid string representation of the original number using the specified base.