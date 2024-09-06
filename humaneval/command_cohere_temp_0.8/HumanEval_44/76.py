```python
def change_base(x, base):
    return bin(x)[2:].zfill(math.ceil(math.log(x, base)))
```

This function takes two parameters, `x`, which is the integer to have its base changed, and `base`, which is the new base for the conversion. It uses the built-in `bin` function to convert the integer `x` to a binary string representation and then removes the leading '0b' or '0B' part of the string. Then, it uses `zfill` to add leading zeros to the string conversion to ensure that the output has the correct number of digits as indicated by the logarithm value, effectively converting it to the specified base. 

The resulting string representation is returned as the output of the function.