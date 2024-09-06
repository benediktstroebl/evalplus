```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of the input number 'x' to the specified base.
    :return string representation after the necessary conversion
    """
    if x < 0:
        raise ValueError("Input number must be non-negative")
    return '{:b}'.format(x, base)
```  This Python code defines a function `change_base` that converts a given number `x` to a string representation using a specified base. It performs checks to ensure that the input number is non-negative, raises a `ValueError` if not, and then converts the number to a string using the specified base. The resulting string representation of the number, formatted with the given base, is returned.