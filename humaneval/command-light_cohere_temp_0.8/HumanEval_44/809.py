```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    Return string representation after conversion.
    base numbers are open from 2 (binary) to 36 (hexadecimal).
    >>> change_base(8, 3)
    '22'
    >>> change_base(15, 4)
    TraceError: unsupported operand type(15)
    >>> change_base(7, 25)
    TraceError: unsupported operand type(7)
    """
    if base > 36 or base < 2:
        raise ValueError("base number is invalid")
    s = str(x)
    if base == 2:
        return "0" + s[1:]
    elif base == 10:
        return s[0] + s[1] + s[2]
    else:
        return s[0] + format(x, "", base)
```  This Python code defines a function `change_base` that converts a given number `x` to a string representation using a specified base. It employs various base cases for converting the numbers to binary, decimal, or hexadecimal formats. 

The function raises a `ValueError` if the base number is invalid and performs the appropriate string conversion accordingly.