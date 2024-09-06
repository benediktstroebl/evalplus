```python
def change_base(x: int, base: int):
    """Change the numerical base of input number x to base base.
    return string representation after conversion.
    base numbers are optimal for 10.
    >>> change_base(8, 3) == '22'
    >>> change_base(8, 2) == '1000'
    >>> change_base(7, 2) == '111'
    True
    """
    # Implementation
    result = ""
    while x > 0:
        whole = x % base
        remainder = x // base
        result = str(remainder) + result
        x = whole
        if remainder != 0:
            result = result[:-1] + '0' + result[1:]
    return result
```