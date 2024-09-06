Here is a Python script that defines a function change_base that converts a number to a string representation using a specified base:
```python
def change_base(x, base):
    """
    Change numerical base of input number x to base.
    Return string representation after conversion.
    base numbers less 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    return format(x, f"{base}")
```