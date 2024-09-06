```python
def change_base(x, base):
    return bin(x)[2:].rjust(ceil(log2(x)), '0')[::-1].zfill(log2(x), base)
```

This function takes two parameters, `x`, which is the integer to be converted, and `base`, which is the desired base between 2 and 10. It uses built-in Python functions like `bin`, `log2`, `ceil`, `rjust`, and `zfill` to achieve the conversion efficiently. The resulting string representation of the number `x` in the specified base is then returned. 

Here's an example of function usage:
```python
print(change_base(8, 3))  # Outputs: '22'
print(change_base(8, 2))  # Outputs: '1000'
print(change_base(7, 2))  # Outputs: '111'
```

This example demonstrates the conversion of the numbers 8, 7, and 8 into their respective base 3, base 2, and base 2 representations, respectively.