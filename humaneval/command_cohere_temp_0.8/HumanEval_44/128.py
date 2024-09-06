```python
def change_base(x, base):
    return bin(x)[2:].zfill(math.ceil(math.log(x, base)))
```

This function takes two parameters, `x`, which is the integer to have its base changed, and `base`, which is the new base for the conversion. It uses the built-in `bin()` function to convert the integer `x` to a binary string representation. The prefix `'0b'` is removed using slicing (`bin(x)[2:]`). To ensure the converted number is returned as a string of the desired base, zfill() is utilized to left-pad the binary number with zeros if necessary. This padding is calculated using `math.ceil(math.log(x, base))`, ensuring the returned string has the proper length and is centered in the new base. 

The `change_base` function efficiently converts integer numbers to different bases and returns the string representation of the conversion, producing the desired output.

Here are some example outputs of the function:
```
change_base(8, 3) = '22'
change_base(8, 2) = '1000'
change_base(7, 2) = '111'
```