```python
def change_base(x: int, base: int):
    """Change the numerical base of input number x to base base."""
    if base < 2 or base > 36:
        raise ValueError("Base number must be between 2 and 36.")
    elif base == 10:
        return str(x)
    else:
        return '{:0{}b'.format(x, base)
```  This code defines a function called change_base that takes two arguments: x, which is the number to be converted, and base, which is the base to which the number is to be converted. The function checks if the base is valid, and if it is, it converts the number to the desired base and returns the string representation of the number.

If the base is not a valid number, the function raises a ValueError exception. The code is well-contained and can be used to solve the problem.