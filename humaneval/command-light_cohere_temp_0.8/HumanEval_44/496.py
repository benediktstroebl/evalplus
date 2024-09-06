```python
def change_base(x: int, base: int):
    """
    Change the base of a number to another base
    :param x: int - Numerical number
    :param base: int - New base to convert to
    :return: string representation
    """
    # whole number to base conversion
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")
    # check for negative numbers
    elif x < 0:
        x = abs(x)
    # apply conversion
    return format(x, f'{base}')

# Test the function
try:
    print(change_base(-8, 2))
    print(change_base(123, 10))
    print(change_base(10, 2))
    print(change_base(0, 7))
    print(change_base(5, 35))
except ValueError as ve:
    print(ve)
```
The code defines a function `change_base` that converts a given number to a new base. The function first checks if the specified base is within the valid range (2 to 36). If the base is invalid, a `ValueError` exception is raised. The function also checks if the input number is negative, and converts it to its absolute value. The function then uses the `format` function to convert the number to the specified base. The output is a string representation of the number in the desired base.