```python
def change_base(x, base):
    return str(x).translate(str.maketrans('123456789', f'{base}_{base}_{base}_{base}_{base}_{base}_{base}_{base}'))
```

This approach uses string translation, which is efficient and works without importing any extra libraries. The `str.maketrans` method is used to create a translation table that maps digits `123456789` to the desired base digits. For example, if `base` is 3, it maps `123456789` to `33322233322221`. Then, the function `str.translate(table)` is called on the input number `x` to change its base.