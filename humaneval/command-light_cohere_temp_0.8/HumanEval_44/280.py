Here's the code:
```python
def change_base(x: int, base: int) -> str:
    """Change the base of integer x to base base and return the string representation."""
    # Use math.isin(x) to convert to string and to convert to uppercase
    return f'{x:>{base}' if type(x) == int and base <= 36 else 'Invalid base number'
```
This code provides a self-contained function `change_base` that takes an integer `x` and an integer `base` as parameters. The function converts the `x` to a string using `f'{x:>{base}'` and checks if the base is less than or equal to 37. If the type of `x` is an integer and the base is within the range of base numbers, it returns the string representation of `x` in the desired base. If the input is not an valid number or an invalid base number, it returns an error message.