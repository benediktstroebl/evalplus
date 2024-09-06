```python
def change_base(x: int, base: int) -> str:
    """
    Convert a number to a string with the desired base.
    Args:
        x: int, number to be converted
        base: int, desired base for the output string
    Returns: 
        str: converted string representation
    """
    # ensure base is not 0 or negative
    if base < 0:
        raise ValueError("Base must be positive")
    if base == 0:
        base = 10  
    # handle negative numbers
    x = abs(x)
    # generate string representation
    string = "{0:>{format(x, '{base}',10)}".format(x, (base,))
    return string

#unit tests
print(change_base(8, 3))      # 22
print(change_base(128, 3))     # 64
print(change_base(-7, 2))     # -111
print(change_base(10, 0))      # 10
print(change_base(30, 4))      # 030
print(change_base(5, 1))      # 05
print(change_base(0, 16))     # 000000
print(change_base(3, 16))     # 000000016
```