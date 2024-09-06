```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base B.
    return string representation after conversion.
    base numbers are
        for 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(9, 5)
    Traceback (most recent call last):
      File "<stdin>", line 6, in <module>
        9
    ValueError: unsupported literal for int() with base 5: '9'
    """
    try:
        return str(x)
    except ValueError:
        raise ValueError("Unsupported literal for int() with base.")
```