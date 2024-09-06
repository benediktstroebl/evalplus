Here's a self-contained Python script with a function that solves the problem of changing the base of a number to another base:
```python
def change_base(x: int, base: int):
    """
    Change the base of the input number x to base base.
    Return a string representation after conversion.
    base numbers 10 and
    return as string.
    """
    def convert(x: int, base: int):
        """
        Convert integer x to string representation in base b.
        """
        return f"{x{x}".format(f"{x:{base}}")
        """
        return f"{x:{base}}"
    return convert(x, base)
```

This script defines a function `change_base`, which takes two arguments: `x`, which is the number to be converted, and `base`, which is the base to which the number will be converted. The function uses the `convert` function to convert the number to a string representation using the desired base. 

The `convert` function takes an integer `x` and a base `base` as input and returns the string representation of `x` in the specified base.

This function allows you to easily change the base of a number to another base. 

Please note that the code is self-contained and does not require any additional variables or functions to solve the problem.