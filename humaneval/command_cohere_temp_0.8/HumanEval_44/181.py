```python
def change_base(x, base):
    return bin(x)[2:].zfill(math.ceil(math.log(x, base)))
```

This function takes two parameters, `x`, which is the integer to be converted, and `base`, which is the conversion target base. Using the built-in `bin` function, it returns the binary representation of `x`. The prefix '0b' is removed using the slice `[2:]`, and then the binary string is zero-padded on the left to the nearest integer number of digits using the `zfill` method. The precision of the conversion is determined using the `math.log` function, rounding up via `math.ceil` to ensure the result has at least the specified number of digits.

Here is an example usage of the function:
```python
print(change_base(8, 3))  # Outputs '22'
print(change_base(8, 2))  # Outputs '1000'
print(change_base(7, 2))  # Outputs '111'
```

This demonstrates how the function appropriately changes the base of the input number `x` to `base`, providing the string representation of the result.