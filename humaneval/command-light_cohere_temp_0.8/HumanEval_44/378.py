```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    return string representation after conversion.
    base numbers other in 10
   
    >>> change_base(8, 3)  # Base 3
    '22'
    >>> change_base(8, 2)  # Base 2
    '1000'
    >>> change_base(7, 2)  # Base 2
    '111'
    >>> change_base(123, 5)  # Base 5
    '555'
    >>> change_base(123, 0)  # Error: invalid base number
    """
    if base < 2 or base > 36:
        raise ValueError("Invalid base number")

    return '{:b}'.format(x, base)
```