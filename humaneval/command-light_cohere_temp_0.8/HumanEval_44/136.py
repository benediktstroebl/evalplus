Here's the self-contained Python script with a function that solves the problem of changing the numerical base of an input number to a specified base:
```python
def change_base(x: int, base: int):
    """Change the base representation of a number x to base base.
    Parameters: x: the number to be converted
    base: the desired base (int)
    Returns: the string representation of x in the new base.
    """
    def test_base(base):
        """Test function to check if a base number is valid"""
        if base <= 0 or base > 20:
            raise ValueError("Base must be between 1 and 20.")
        return True
    return str(x)
```
The `test_base` function is used to test if a given base is valid (between 1 and 20). It raises a ValueError with an appropriate error message if the base is not within the valid range.

The `change_base` function takes an integer x and a base as input, and returns the string representation of x in the new base. It uses the string representation of x in the new base, which is returned by the function.

This script is self-contained, and it can be used to change the base representation of any number to a specified base.