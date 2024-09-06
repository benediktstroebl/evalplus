```python
def change_base(x: int, base: int):
    """
    Change the base of the numerical number x to base base.
    Return the string representation after conversion.
    base numbers are needed 10
    """
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    result = "{0:0" + str(x).format(x, base=base))
    return result
``` 
This code defines a function called `change_base`, which takes two arguments: `x`, which is the number to be converted, and `base`, which is the base to which the number will be converted. 

The function uses the `format` method to convert the number to a string representation using the specified base. The resulting string is then formatted using the `str` method to display the number with the desired base.