```python
def change_base(x: int, base: int):
    if not isinstance(x, (int, float)) or x < 0:
        raise TypeError("Input must be a non-negative number")
    if not isinstance(base, int) or base < 2 or base > 36:
        raise TypeError("Base number must be an integer greater than or equal to 2 and less than 36")

    if base == 2:
        return '{:02}'.format(x)
    elif base == 10:
        return '{:05}'.format(x)
    elif base == 16:
        return '{:04x}'.format(x)
    elif base == 32:
        return '{:07}'.format(x)
    elif base == 64:
        return '{:08}'.format(x)
    elif base == 96:
        return '{:09}'.format(x)
    elif base == 128:
        return '{:0{}f}'.format(x)
    else:
        return '{:{}f}'.format(x, base)

x = 8
base = 2

print(change_base(x, base))
``` 
This function changes the base of the input number x to the specified base, and then returns the string representation of the result.