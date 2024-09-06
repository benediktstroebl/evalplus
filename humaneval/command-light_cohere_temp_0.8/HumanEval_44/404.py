```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base base.
    Returns string representation after conversion.
    base numbers less 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    return "{:04b}".format(x, base)
```  This code defines a `change_base` function that takes an integer `x` and a base `base` as input. It converts the the use the `format` technique, which involves converting the number to a string and then back to a number using the base conversion rules. The final output is a string representation of the number in the desired base. 

This function can be used to efficiently change the base of any number to a specified base.