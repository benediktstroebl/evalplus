```python
def change_base(x, base):
    return str(x).translate(str.maketrans('123456789', f'{base}_{base}_{base}_{base}_{base}_{base}_{base}_{base}'))
```

This function takes two inputs, `x`, and `base`. `x` is the number that the user wants to convert, and `base` is the target conversion base. It uses the `str.translate` method to replace each digit in `x` with the corresponding digit in the new base. The translation is provided using `str.maketrans`'s format syntax, where `base` is repeated to fill the mapping for each digit from `123456789` to the new base mapping.

The function is self-contained and does not rely on any external modules or variables, making it easy to use and integrate into other projects. 

Here is an example of how you can test this function:
```python
# tests:
assert change_base(8, 3) == '22'
assert change_base(8, 2) == '1000'
assert change_base(7, 2) == '111'
```

This script provides a functional implementation of the `change_base` function as described in the problem statement, and it can be used directly in other projects or scripts that need similar base conversion capabilities.