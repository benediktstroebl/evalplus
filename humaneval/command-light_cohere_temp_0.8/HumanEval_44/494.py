```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number x to base b.
    >>> change_base(8, 3) == '22'
    True
    >>> change_base(8, 2) == '1000'
    True
    >>> change_base(7, 2) == '111'
    True
    """
    return "{:b}".format(x, base)
```  This script defines a function called change_base, which takes two arguments: x, which is the number to be converted, and base, which is the desired base for the conversion. 

The function returns the string representation of the number in the specified base, which is checked against the provided test strings using the == operator.