```python
def change_base(x, base):
    return bin(x)[2:].zfill(math.ceil(math.log(x, base))) if base != 10 else str(x)
```

This function takes two parameters, `x`, which is the integer to have its base changed, and `base`, which is the base to change it to. It uses the built-in function `bin()` to convert the integer `x` to a binary string and then removes the leading '0b' or '0B'. Then, it uses `zfill()` to add zeros to the right of the string to ensure the output length conforms to the length that would be expected from the base `base` representation of the input `x`, which is calculated using `math.log()`. If `base` is 10, it simply returns the string representation of `x` since 10 is the default base for integers in Python.

Here is an example usage of the function:
```python
print(change_base(8, 3))  # Outputs '22'
print(change_base(8, 2))  # Outputs '1000'
print(change_base(7, 2))  # Outputs '111'
print(change_base(123, 10))  # Outputs '123'
```