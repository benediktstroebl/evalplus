Here is a Python script that includes a self-contained function to convert the input number to a string using a specified base:
```python
def change_base(x, base):
    """
    Convert a number to string representation with specified base.
    """
    number as a int -> string, base is a digit base (e.
    """
    example:
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    return '{:b}'.format(x, base)
```

This script defines a `change_base` function that takes two arguments: the number `x` to be converted and the desired base `base`. The function uses the `:` operator to convert the number to a string and then applies the `format` method to format the number with the specified base.