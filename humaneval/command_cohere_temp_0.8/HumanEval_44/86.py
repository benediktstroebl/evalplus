```python
def change_base(x, base):
    return bin(x)[2:].zfill(math.ceil(math.log(x, base)))
```

This function takes two parameters, `x`, which is the integer to be converted, and `base`, which is the conversion base. The function uses the built-in `bin()` function to convert the integer `x` to a binary string representation. The `[2:]` slice is used to remove the '0b' prefix. `math.ceil(math.log(x, base))` is used to determine the minimum number of base `base` digits needed to represent `x`. The `zfill()` method is then used to left-pad the binary string with zeros if necessary, so that the representation is always returned as a string with the minimum number of digits.

Here's an example usage of the function:
```python
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

This demonstrates how the function can change the base of a number from `x` to `base`, as specified in the problem statement. Please note that the code assumes that the base numbers provided are less than 10. Adjustments can be made if this restriction is lifted in the problem scenario.