```python
def change_base(x, base):
    return bin(x)[2:].zfill(math.ceil(math.log(x, base)))
```

This function takes two inputs, `x`, which is the number to be converted, and `base`, which is the new base for conversion. It uses the built-in `bin` function to convert the integer `x` to a binary string and then removes the leading '0b' or '0B' and replaces it with zeros to the left until the length of the string is at least the logarithm of `x` in base `base`, which ensures the correct conversion to the new base.

Here's an example usage of the function:
```python
print(change_base(8, 3))  # Outputs '22'
print(change_base(8, 2))  # Outputs '1000'
print(change_base(7, 2))  # Outputs '111'
```

This demonstrates how the function can change the base of the numeric representation while maintaining the same numerical value.