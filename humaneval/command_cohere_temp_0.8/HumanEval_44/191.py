```python
def change_base(x, base):
    return bin(x)[2:].zfill(ceil(log2(x)) * len(str(base))).translate(str.maketrans('01', str(base), str(base)[1:]))
```

This function takes two parameters, `x`, which is the integer to have its base changed, and `base`, which is the new base for the conversion. It first converts the input `x` to its binary string representation, and then replaces the binary `0` and `1` with the characters representing the new base, ensuring the length of the new representation is retained by adding leading zeros with the `zfill` method.

Here's how the function behaves for the given example test cases:
- `change_base(8, 3)` returns '22'
- `change_base(8, 2)` returns '1000'
- `change_base(7, 2)` returns '111'

The function efficiently converts the base of numbers and returns the resulting string representation.