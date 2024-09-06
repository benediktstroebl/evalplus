```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    return string representation after conversion.
    base numbers less 10
    I've seen this problem
    >>> change_base(8, 3)
    '22'
    >>> change_base(16, 4)
    TraceError: 'int' object does not support item assignment with '+'
    """
    return '{:0b}'.format(x, base)
```