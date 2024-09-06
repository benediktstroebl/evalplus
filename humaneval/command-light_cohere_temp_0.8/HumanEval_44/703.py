```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base.
    Args: 
        - x: int, the number to be converted 
        - base: int, the base to convert to
    Returns: 
        - string representation of the number in the specified base
    """
    # check if base is valid
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")
        
    # calculate the representation in the new base
    if base == 10:
        return str(x)
    elif base == 2:
        return str(x, 2)
    else:
        return str(x, int(base))

# unit tests
print(change_base(8, 3))    # expected output 22
print(change_base(8, 2))   # expected output 1000
print(change_base(7, 2))   # expected output 111
print(change_base(10, 3))  # expected output 300
print(change_base(100, 10)) # expected output 10100
print(change_base(10, 32)) # expected output 30000000000
```