```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base base.
    """ return string representation after conversion
    base numbers use 10
    """
    return "{:0>}"[x].translate(str.format(base))
```
This function, `change_base`, takes two arguments: `x`, which is the number to be converted, and `base`, which is the base to which the number is to be converted. It then uses the format() function to convert the number to a string representation with the specified base.