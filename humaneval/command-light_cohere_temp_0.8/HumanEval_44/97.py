```python
def change_base(x: int, base: int):
    if not isinstance(x, int) or not isinstance(base, int):
        raise TypeError("Input must be an integer")
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")
    return str(x) if x < base else str(x).base) + str(x - base)
``` 
This code defines a function `change_base` that converts a number to a string representation using a specified base. The function ensures that the input is an integer and that the base is within a valid range. 

Then it returns the resulting string representation of the number using the specified base.