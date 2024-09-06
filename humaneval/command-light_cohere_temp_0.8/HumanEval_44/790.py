```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of the number x to the base specified.
    Args:
        x: int or string representing a number
        base: int representing the desired base
    Returns:
        str: the string representation of the number with the new base
    """
    if not isinstance(x, str):
        x = str(x)

    if not isinstance(base, int) or base < 2 or base > 36:
        raise ValueError("The base must be a positive integer between 2 and 36.")

    new_base = str(base)
    return x.format(x_str(x, new_base)
```  The function utilizes the `str.format()` method to convert the input number `x` into a string using the specified base `base`. The function ensures the base is a positive integer within the specified range before applying the conversion.