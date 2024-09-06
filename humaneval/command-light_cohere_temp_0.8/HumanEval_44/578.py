```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base.
    Args:
        x: int (number to be base)
        base: int (desired base for conversion)

    Returns:
        str: string representation of the number in the desired base
    """
    if base == 10:
        return str(x)
    elif base == 2:
        return ''.join((x // 1) + 1) * '00'
    else:
        raise ValueError("Invalid base. Provide a base of either base 10 or 2.")

x = 8
base = 3
result = change_base(x, base)
print(result)
``` 
This function will return the string representation of the number in the desired base. For bases other base 10, the number remains as is. For bases 2, it returns a 'binary' representation.