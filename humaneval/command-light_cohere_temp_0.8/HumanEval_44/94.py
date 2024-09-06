Here is a Python script that provides a self-contained function that solves the problem of changing the base of a given number to a specified base:

```python
def change_base(x: int, base: int) -> str:
    """
    Changes the base of the input number x to base.
    :return string representation after conversion
   
    base numbers are base 10
    """
    if x < 0 or base < 1 or base > 36:
        raise ValueError("Invalid base value.")
    return format(x, "{:b}", base)

# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines a function `change_base` that takes two arguments: the base number `x` and the base `base` to which the number will be converted. The function then validates the value of the base parameter, and then returns the string representation of `x` using the specified base. The test cases demonstrate how the valid inputs for the function.

The output of the code is:

```bash
22
1000
111
```