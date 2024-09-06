```python
def change_base(x: int, base: int):
    """
    Change the base of input number x to base base, 
    and return the string representation.
    """
    base numbers less than 10, so we convert to int(base ** (10 - base)) 
    before doing the conversion.
    """
    return format(f"{{:0{}d}".format(x * int(base) ** (10 - base)), -1))
```