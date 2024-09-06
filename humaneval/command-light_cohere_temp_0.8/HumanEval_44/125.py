```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base base.
    Returns string representation after conversion.
    base numbers are numbers less 10
    """
    return format(x, base)
```
The function `change_base` takes two parameters: `x` (the number to be converted) and `base` (the desired base for conversion). It uses the built- `format` format specifier to convert the number to a string, and then applies the desired base to the string. The result is then returned as a string.