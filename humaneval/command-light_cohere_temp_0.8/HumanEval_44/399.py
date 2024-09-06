```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number x to base base.
    >>> change_base(8, 3) == '22'
    True
    >>> change_base(8, 2) == '1000'
    True
    >>> change_base(7, 2) == '111'
    True
    """
    if base > x or base < 2 or base <= 0:
        raise ValueError("Invalid base value.

    bases = [str.join _ string bases in reverse order from base^10)
    result = '0'
    for i in range(1, x+1):
        result = chr(ord(bases[i % len(bases)])+result[::-1][::-1][i % base])
    return result
```