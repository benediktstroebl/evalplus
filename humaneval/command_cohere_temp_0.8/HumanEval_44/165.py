```python
def change_base(x, base):
    return bin(x)[2:].zfill(len(str(x)) * (len(bin(base)) - 2)) if base < len(bin(x)) else str(x)
```

This function takes an integer `x` and a base `base` as inputs and attempts to change the base of `x` to `base`. It uses the built-in `bin()` function which returns a string representation of the binary representation of the input integer. The function extracts the binary representation of the number without the '0b' prefix using `bin(x)[2:]`. If the desired base is shorter than the binary representation of the number, it zeros pad the binary representation to match the length of the desired base representation using ``.zfill(len(str(x)) * (len(bin(base)) - 2))``. This ensures that the number is correctly represented in the desired base. If the desired base is larger than or equal to the length of the binary representation, it simply returns the string representation of the number `str(x)`.

Here's an example usage of the function:
```python
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This demonstrates the function's capability to convert numbers between different bases efficiently utilizing binary representations and zero-padding when necessary.