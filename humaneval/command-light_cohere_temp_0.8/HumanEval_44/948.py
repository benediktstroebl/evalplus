Here is a self-contained Python script that solves the problem of changing the numerical base of an input number to a specified base:
```python
def change_base(x, base):
    """Changes the base of the input number x to the base provided.
    Args: 
        - x: any, number or string, 
        - base: an integer base
    Returns: 
        - string: the number in the specified base
    """
    if isinstance(x, str):
        # Convert string to integer
        x = int(x)
    if x < 0 or base < 2:
        raise ValueError("Invalid input. A number or By not be negative or a number less than 0, or a base less than 2.")
    return "{:,.0f}".format(x, base)
```
This script defines a function called change_base that takes two arguments: x, which is the number to be converted, and base, which is the desired base for the number.

The function first checks if the input arguments are of type string, and if so, it converts the string to an integer using the int() function. If the arguments are integers, the function checks if the number is negative or the base is less than 2, and if so, it raises a ValueError exception with the appropriate error message. 
Finally, the function returns the formatted string representation of the number in the desired base.