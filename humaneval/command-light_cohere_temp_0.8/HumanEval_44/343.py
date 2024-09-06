```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    Return string representation after conversion.
    base numbers less 10 or adds digits before and after for conversion.
    """
    take a number in base and calculate the equivalent number using the given base.
    return the number as a string representation.
    """
number = int(x)
    base = int(base)
    # Calculate equivalent number using the conversion
    num_str = "{0:05b}".format(base ** number)
    return num_str
```