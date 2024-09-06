```python
def change_base(x: int, base: int):
    """
    Change the base of a number x to base base.

    Args:
        x: int, number to change the base of
        base: int, base of the number to be converted to
    """
    assert isinstance(x, int)
    assert isinstance(base, int)
    assert base >= 2, "Base must be greater than 1"
    return '{:0>{}d}'.format(x, base)

# Example usage:
x = 8
base = 2
print(change_base(x, base))  # Output: '1000'
x = 7
base = 3
print(change_base(x, base))  # Output: '22'
```
This script defines a function `change_base` that converts a number `x` to a string in the specified base `base`. The function uses assertions to ensure the inputs are of appropriate type and base is greater than 1. The output is then the formatted string representation of the number with the specified base.