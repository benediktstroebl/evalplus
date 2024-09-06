```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of integer x to base base and returns the result as a string.
    """
    number = x  # convert x to a number (int)
    return '{:b}'.format(number, base)  # format the number with base representation
```
Test cases are included to show how the function works with different inputs and bases.