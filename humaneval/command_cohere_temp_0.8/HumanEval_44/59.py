```python
def change_base(x, base):
    return bin(x)[2:].rjust(ceil(log2(x)), '0')[::-1].zfill(log2(x), base)
```

The function takes two arguments: `x`, which is the integer to be converted, and `base`, which is the desired base. It uses the built-in `bin` function to convert the integer `x` to a binary string and extracts the relevant part of the string with `bin(x)[2:]`. The string is then right-justified to the length of the binary logarithm of `x` (obtained with `log2(x)`), using zeros for padding with `rjust`. This ensures that the output string length is a reasonable representation of the binary value. Finally, it reverses the string and adds zeros to the left (zfill) to ensure the final output is a string of the desired base. 

The expected behavior for the test cases provided in the prompt is:
```
't22'
'1000'
'111'
```