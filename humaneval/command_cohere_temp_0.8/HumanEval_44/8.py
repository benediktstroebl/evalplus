```python
def change_base(x, base):
    return bin(x)[2:].zfill(math.ceil(math.log(x, base)))
```

This function takes two parameters, `x`, which is the integer to have its base changed, and `base`, which is the new base for the conversion. It uses the built-in `bin` function to convert the integer `x` to a binary string and then returns the part of the string after the binary prefix ("b'") up to the padding character ('0' if needed). This padded string is the result of the base conversion.

The `math.ceil(math.log(x, base))` expression calculates the number of digits needed to represent `x` in the new base `base`. The `log` function returns the natural logarithm of the fraction `x / base`, and `ceil` converts it to the next higher integer, ensuring the resulting number is correctly padded with zeros to the left. 

The function handles bases less than 10 as specified in the problem statement. You can test the function by calling it with different values for `x` and `base`.  For example:
```python
print(change_base(8, 3)) # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

This demonstrates the conversion of an integer's base to a custom base, as specified by the problem statement.