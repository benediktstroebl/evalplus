```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    return string representation after conversion.
    base numbers are other use 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    True
    """
    # convert integer to string
    s = str(x)
    # remove trailing spaces
    s = s.replace(' ', '')[:-1]
    # append base to string
    s = s + base
    # convert string to integer and return
    return int(s)
```