```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base base.
    return string representation after conversion
   
    base numbers less than 2 don't have a legal representation, so they will be returned as is.
    """
    # Use the base as an integer
    if base <= 0:
        return ''
    if base > 36:
        base = base - 36
    return '{:0b}'.format(x, base)
```