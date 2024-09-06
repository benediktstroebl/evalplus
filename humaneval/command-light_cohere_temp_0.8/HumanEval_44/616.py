```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base
    specified by base.

    :Return: Converted string representation of x in the new base.

    """
    test cases:
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(-8, 2)
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type( None, int )
    """
    if base == x == int(x):
        return x
    
    if base < 0 or base > getbit(x) or base < getbit(x) or base > 9:
        raise ValueError("Invalid base value.")
    
    sign = 1 if x < 0 else -1
    base = str(base)
    
    if base == '0': base = ''
    elif base == '1': base = '10'
    
    return f"{sign:02}{x:08}{base}"
```