```python
def change_base(x: int, base: int) -> str:
    """
    Changes the base of a number to another base and returns a string representation.
    Args: 
        - x: int (number to be converted)
        - base: int (the base to which convert the number)
    Returns: 
        - str (string representation of the converted number)
    """
    if base > x:
        raise ValueError("Base must be less than or equal to the number")
    if base < 2 or base > 36:
        raise ValueError("Base must be a valid number between 2 and 36.")

    s = str(x)
    return s if s.isle(base) else s[:0] + ''.join(base)
```
This function takes two parameters - x, which is the number to be converted, and base, which is the base to which the number will be converted. It uses the str() function to convert the number to a string, and then applies the base to the number. The function returns the string representation of the converted number.