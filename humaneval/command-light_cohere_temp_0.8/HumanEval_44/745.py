```python
def change_base(x: int, base: int):
    """
    Change the base of the given number x to the specified base.
    Parameters:
    x: int, base: int
    Returns:
        str: string representation of the number with the specified base.
    """
    Example an integer number and a string base representation of numbers 
    using the specified base.
    """
    raise ValueError if the necessary number of arguments is not correct
    """
    assert len(x) == 1 and len(base) == 2, "Two arguments required: (number, base)."
    return "{0:02x}".format(x, base)

# Test the function
print(change_base(8, 3))  # Output: 22
print(change_base(7, 2))  # Output: 111
print(change_base(5, 10)) # Raises ValueError
```