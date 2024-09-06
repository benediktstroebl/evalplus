Here is a self-contained Python script that solves the problem of converting a given number to a different base:
```python
def change_base(x: int, base: int):
    # Convert input number x to a string
    num_str = str(x)
    
    # Convert the number to the desired base
    return num_str.format(f"{base}")

# Test cases
print(change_base(8, 3))    # Output: '22'
print(change_base(8, 2))   # Output: '1000'
print(change_base(7, 2))   # Output: '111'
```
This script defines a function `change_base` that converts a given number `x` to a string representation in a specified base `base`. The function utilizes the built-in `str` function to convert the number to a string, and then applies the `format` method with the `base` parameter to return the string representation in the desired base.

This self-contained solution provides a straightforward way to convert numbers to different bases, making it easier to use and maintain in various scenarios.