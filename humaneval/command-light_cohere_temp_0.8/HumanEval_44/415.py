```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    return string representation after conversion
   
    base numbers less than 2 yield the string representation directly, 
    while others are computed using the listing of digits in the given base.
    """
    number = str(x)
    for c in '0123456789abcdef':
        number = number.replace(int(c),
        base)
    return number
```