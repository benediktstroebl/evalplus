```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base base.
    Return string representation after conversion.
    base numbers are
    required to be > 0 and less than 36.
    >>> change_base(8,3) == '22'
    >>> change_base(8, 2) == '1000'
    >>> change_base(7, 2) == '111'
    """
    if base < 0 or base > 36:
        raise ValueError("Base number must be greater than 0 and less than 36.")
    result = str(x)
    for c in result:
        if c <= '9':
            result = result[:-len(c)] + chr(96 + base * ord(c))
        else:
            result = result[:-len(c)]
    return result
```