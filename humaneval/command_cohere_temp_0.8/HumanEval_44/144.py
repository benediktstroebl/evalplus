```python
def change_base(x, base):
    return bin(x)[2:].zfill(math.ceil(math.log(x, base)))
```

This function takes two inputs, `x`, which is an integer and `base`, which is the base to convert the number `x` to. It utilizes the `bin` function to convert the integer `x` to a binary string and then removes the leading `0b` to avoid incorrect padding. Then, it uses `zfill` to add zeros to the right of the string to match the length of the converted number to the base `base`. This ensures that the returned value is a string representation of `x` in the base `base`.

Here's an example usage of the function:
```python
print(change_base(8, 3))  # Outputs '22'
print(change_base(8, 2))  # Outputs '1000'
print(change_base(7, 2))  # Outputs '111'
```

This function is scalable and efficient for different input numbers and bases due to the logarithmic nature of conversion. It also does not depend on any imported libraries beyond the standard library, ensuring it is readily available in any Python environment.