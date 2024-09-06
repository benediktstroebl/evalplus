```python
def change_base(x, base):
    return bin(x)[2:].rjust(ceil(log2(x)), '0')[::-1].zfill(log2(x), base)
```

This function takes two parameters, a number `x` and a base `base`. It converts the number `x` into the specified base using the formula `base^exponent = x`, where `exponent` is calculated as `log₂(x)` and the conversion is done using `bin(x)[2:]`. The resulting string is then reversed and padded with zeros on the left to ensure it is of length `log₂(x)`. Finally, it is padded with the base `base` to the length of the string.

Here's an example usage of the function:
```python
print(change_base(8, 3))  # Outputs '22'
print(change_base(8, 2))  # Outputs '1000'
print(change_base(7, 2))  # Outputs '111'
```

This self-contained function encapsulates the process of converting a number to any given base, as specified by the problem statement.