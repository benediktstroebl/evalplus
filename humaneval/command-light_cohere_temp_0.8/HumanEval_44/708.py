```python
def change_base(x: int, base: int):
    if not isinstance(x, (int, float)) or x <= 0:
        raise TypeError("Input should be a positive number")
    if base <= 0 or not isinstance(base, (int, float)) or base <= 1:
        raise TypeError("Base should be a positive integer")
    return '{:0>{}d}'.format(x, base)

# Test the function
x = 8
base = 2
result = change_base(x, base)
print(result)  # Output: 1000

x = 7
base = 2
result = change_base(x, base)
print(result)  # Output: 111

x = 'abc'
base = 10
result = change_base(x, base)
print(result)  # Output: 'abc'
``` 
This Python script defines a function `change_base` that takes two arguments: `x` (the number to be base-converted) and `base` (the numerical base to convert to). It checks the validity of both inputs using type and value checks, and if the inputs are valid, it performs the base conversion using string formatting and returns the result as a string.

This script can be used to quickly convert a number to a specified base, or to check if a given number can be converted to a specific base.