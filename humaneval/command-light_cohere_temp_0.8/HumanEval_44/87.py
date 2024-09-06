```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base.
    Parameters:
        x: int, the number to change the base of
        base: int, the base to which the number will be changed to
    Returns:
        string, the number converted to the new base
    """
    # Convert the number to a string using the given base
    return str(x, base)

# Test the function with some cases
assertEqual(change_base(8, 3), '22')
assertEqual(change_base(8, 2), '1000')
assertEqual(change_base(7, 2), '111')
assertEqual(change_base(-5, 2), '-20')
assertEqual(change_base(10, 5), '602')
assertEqual(change_base(3, 7), '777')
```

This code defines a function `change_base` that takes two arguments: a base number and a number to be converted. It then converts the this number to a string using the specified base and returns the converted string.