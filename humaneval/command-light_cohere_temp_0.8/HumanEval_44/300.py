```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base B.
    Return string representation after conversion.
    base numbers are for 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(9, 10)
    Traceback (most recent call last):
    TypeError: 'int' object does not support item assignment
    """
    raise TypeError("Input must be an integer")
```