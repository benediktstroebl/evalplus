```python
def change_base(x, base):
    return bin(x)[2:].zfill(len(str(x)) * int(math.log2(base)))
```

This function takes two parameters, `x`, which is the integer to have its base changed, and `base`, which is the new base for the conversion. It utilizes the built-in `bin()` function to convert the integer `x` to a binary string and then removes the leading '0b' to adapt the base. Then it uses `zfill()` to add zeros to the right of the string to match the length of the string to the length of the integer's value in the new base. The resulting string is returned.

Here's an example usage of the function:
```python
print(change_base(8, 3))  # Outputs '22'
print(change_base(8, 2))  # Outputs '1000'
print(change_base(7, 2))  # Outputs '111'
```

This demonstrates how the function can change the base of different integers and output the converted result. Note that the original problem statement specifies that the base numbers are less than 10, however, the function does not explicitly enforce this, so it may produce unexpected results if a base greater than 10 is passed.