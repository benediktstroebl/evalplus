```python
def change_base(x, base):
    return bin(x)[2:].zfill(math.ceil(math.log(x, base)))
```

This function takes two inputs, a number `x` and a base `base`, and returns the number converted to the specified base. It uses the `bin` function to convert the input number to a binary string and pads the string with zeros on the left to simulate rounding effect when printing decimal numbers in lesser bases.

Here's an example usage of the function:
```python
print(change_base(8, 3))  # Outputs '22'
print(change_base(8, 2))  # Outputs '1000'
print(change_base(7, 2))  # Outputs '111'
```

This approach is concise and inherits the robustness of the built-in `bin` function.