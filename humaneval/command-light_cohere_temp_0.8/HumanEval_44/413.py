```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of a number to another base.
    Args:
        x: int, number to be converted
        base: int, target base for conversion
    Returns:
        str, string representation of the converted number
    """
    if base > x // base:
        raise ValueError("Base cannot be greater than number's divisor.")
    if base < 2:
        base = 10 # Default to base 10 if base is less than 2
    # convert to desired base
    return format(x, f"{base}>{int(x) % base}", cur_str=str)
```
The provided Python script defines a function change_base that converts a given number x to a specified base. The base can either be 10 or less than 2, in which case it defaults to base 10. The function performs the mathematical operation x * base^x on the input number, where x is raised to the power of base. It then uses the mathematical operation floor(x) % base to remove the fractional part of the result, and finally, uses the format function to apply the conversion to the desired base.