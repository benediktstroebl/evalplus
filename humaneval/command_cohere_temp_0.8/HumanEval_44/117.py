```python
def change_base(x, base):
    return bin(x)[2:].zfill(len(bin(x)[2:]) * int(base))
```

This function takes two inputs, `x`, and `base`, where `x` is the number to be converted, and `base` is the target base. It uses the built-in `bin()` function to convert the number `x` to a binary string and then removes the leading '0b' from the result. After that, it uses `zfill()` to add zeros to the right of the string to make sure the string length is exactly `len(bin(x)[2:]) * int(base)`, which is the output length the user wants. The result is a string representation of the number `x` in the base given by `base`, as specified by the problem statement.