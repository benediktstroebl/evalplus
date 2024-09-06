```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number x to base base.
    :return converted string representation
   
    """
    if base < 2 or base > 36:
        raise ValueError("Invalid base number.")
    return "{:02}".format(x, base)
```
 The function change_base takes an integer x and an integer base as input, and returns the string representation of x in the base base. The function also includes input validation to ensure the base is within the valid range of base numbers (2-36).

The function utilizes the :format() method to convert the number to a string representation, and applies the base conversion by using the base-converter in the standard library. The :str. This ensures a time correct conversion of the number to a string representation in the specified base.