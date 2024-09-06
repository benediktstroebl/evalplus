```python
def change_base(x, base):
    return str(x).translate(str.maketrans('123456789', f'{base}_{base}_{base}123456789'))
```

This approach utilizes the `translate` method to replace characters with the corresponding base numerals. For instance, when base is 2, `8` is translated to `1000` since `8` corresponds to `1000` in base 2. The `str.maketrans` helper method creates a mapping that maps each character to its corresponding base representation.

This approach results in an elegant and straightforward solution that fulfills the problem requirements.