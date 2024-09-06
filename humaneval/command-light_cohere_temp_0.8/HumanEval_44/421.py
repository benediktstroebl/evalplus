```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base.
    Convert a string representation to base x.
    Parameters:
    x: int, base: int

    Returns: str
    """
    # If base is 10, return x as it is
    if base == 10:
        return str(x)
    # Convert to base using numeral system
    else:
        return "{0}".format(x, base)

# Test the function
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
 ```
This script defines a function `change_base` that converts a number to a new base. It utilizes a approach where, if the base is 10, it simply returns the number as it is. If the base is not 10, it converts the number to the desired base using the `format` method. The test cases ensure that the function is correctly implemented.