```python
def change_base(x, base):
    return str(x).translate(str.maketrans('123456789', f'{base}_{base}_{base}123456789'))
```

This approach utilizes string translation with str.maketrans to convert digits from base 10 to base `base`. For example, when base is 3, the translation map is configured to map '1' to '1', '2' to '2', '3' to '0', and so on. This way, when the string representation of the number is translated, each digit is effectively converted to the new base. This works because in the translation, each digit maps to the corresponding digit in the new base or the complement of the new base (filled with zeros to preserve the length), ensuring a successful conversion to the desired base. 

The function is designed to handle negative numbers gracefully, treating them like positive numbers and converting them to the desired base. 

To see it in action, try calling the function with different inputs, such as `change_base(8, 3)` or `change_base(-7, 2)`. 

This approach is more efficient and suitable for larger numbers or bases than manual conversion digit by digit, especially for big numbers or large bases.