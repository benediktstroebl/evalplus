```python
def change_base(x: int, base: int):
    """
    Change the base numerical representation of input number x to base base.
    return string representation after conversion.
    base numbers are maximum base less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(9, 10)
    '98'
    >>> change_base(35, 2)
    TraceError: unsupported operand type(35) for comparison
    """
    result = str(x)
    if x > 0 and base > 0 and base <= 36 and x <= base:
        result = result[:int(base)] + result[-base:]10 * base
    return result
```