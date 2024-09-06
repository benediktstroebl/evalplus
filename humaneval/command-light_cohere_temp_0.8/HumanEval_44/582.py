Here's the code that implements the function `change_base(x, base)`:
```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base.
    Return string representation after conversion.
    base numbers are: 10, 2
    """
    # Perform the conversion
    base = 10 if base > 10 else base
    # Pad the result with zeros if the number is less than base
    string = '{0}'.join(x).format(x, base=base)
    return string
```
This script provides a simple function to convert a number to a different base. It uses the common base convention of 10 or 2, which you can adjust based on specific requirements. The function formats the string representation in the desired base and returns the result.