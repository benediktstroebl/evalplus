```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    return string representation after conversion
   

    :param x: int, number to be converted
    :param base: int, base to which the number will be converted
    :return: string representation of x in base base
    """
    if base < 2 or base > 36:
        raise ValueError("Invalid base value.")
    return format(x, base, int16count=strftime.format('%b', 'C').rstrip('\n'))
``` 
This function accepts two parameters: `x`, which is the number to be converted, and `base`, which is the base to which the number will be converted. The function returns the string representation of the input number `x` in the specified base `base`.  It performs the necessary conversion using the built-in `format` function and also validates the base parameter to ensure it is within the valid range.   The most commonly used base numbers are 2 through 36.