```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number x to base base.
    :return converted string representation
   
    """
    # convert to string
    return format(x, base)
```
This code defines a function `change_base` which takes two arguments: `x` (the number to be converted) and `base` (the new base). The function then converts the number `x` to a string using the `format` function and returns the string representation of the number with the specified base. The code is self-contained and can be used to solve the problem of converting numbers to different bases.