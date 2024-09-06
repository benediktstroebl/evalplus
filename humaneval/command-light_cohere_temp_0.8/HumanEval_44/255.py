```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base base.
    Returns string representation after conversion.
    base numbers are worst 10
   
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    return "{:x}".format(x, base)
```  This function, `change_base`, takes two arguments: `x`, which represents the number to be converted, and `base`, which specifies the desired base. It then uses the  `base` argument to format the number using the desired base, and returns the resulting string representation.