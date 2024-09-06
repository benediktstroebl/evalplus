```python
def change_base(x: int, base: int):
    """
    Change the numerical base of the input number x to the base specified.
    Args:
        x: int, the number to be converted
        base: int, the base to which the number will be converted
    Returns:
        str: string representation of the converted number
    """
    assert isinstance(x, int) and x >= 0, "Input number must be non-negative integer"
    assert isinstance(base, int) and base >= 2 and base <= 36, "Base must be a positive integer between 2 and 36"

    # Apply binary conversion with 2 as base
    return '{:04b}'.format(x).format(x, base)
```
This Python function `change_base` takes an integer `x` and an integer `base` as input. It checks for the already input conditions: it asserts that the `x` parameter is an integer and non-negative, and the `base` parameter is a positive integer within the range of acceptable base numbers (2 to 36).

The function then performs the conversion, applying the `binary conversion` algorithm, and returns the resulting string representation of the converted number.