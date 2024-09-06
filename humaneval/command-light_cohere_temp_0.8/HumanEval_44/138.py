```python
def change_base(x: int, base: int):
    """
    Change the numerical base of the input number x to the specified base.
    Parameters:
    x: int or string representing a number
    base: int representing the desired base
    Returns: string representation of the converted number
    """
    if isinstance(x, str):
        x = int(x)  # Convert input string to integer
    return "{0:b}".format(x, base)  # Use built-in formatting to get string with base

```

Here, the function takes an integer `x` and an integer `base` as input and returns the converted number with the specified base. The function first checks if the input `x` is a string and then converts it to an integer using the `int()` function. 

This is a common and safe way to handle string inputs in Python, ensuring that the number is treated correctly. 

Finally, the function uses the `format()` method to convert the number to a string with the desired base.