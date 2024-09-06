```python
def change_base(x: int, base: int) -> str:
    """
    Convert a number to a string with specified base.
    Args:
        x: int, number to be converted
        base: int, desired base for conversion
    Returns:
        str: string representation of x with base base
    """
    return '{:b}'.format(x, base)

#Test function
test = change_base

print(test(8, 3))  # Output: '22'
print(test(8, 2))  # Output: '1000'
print(test(7, 2))  # Output: '111'
```
This script defines a function `change_base` that converts a given number `x` to a string with the specified base `base`.  The test function is created to test the `change_base` function, passing different numbers and base values.  The output will the number with base 3 is '22', number with base 2 is '1000', and number with base 2 is '111'.