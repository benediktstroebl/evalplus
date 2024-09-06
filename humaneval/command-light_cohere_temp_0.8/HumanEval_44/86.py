```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    return string representation after conversion.
    base numbers other 1 <= 5
   
    """
    if base > 5:
        return 'base out of range'
    if x < 0:
        return 'negative number'
    s = str(x)
    while len(s) < base:
        s += '0'
    return s
```