Here's a self-contained Python script that provides a function to convert a number to a string representation using a specified base:
```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base
    and return string representation.
    """
    string representation using the example in given base.
    base numbers are 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    # Perform the conversion
    return format(x, f"{base}{int}")
```  # split the format function into two parts: the first argument is the format specifier and the second argument is the formatting code