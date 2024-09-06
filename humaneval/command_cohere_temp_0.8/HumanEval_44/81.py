```python
def change_base(x, base):
    return str(x).translate(str.maketrans('123456789', f'{base}_{base}_{base}123'))
```

This approach uses string translation, which is efficient and works without importing any extra libraries. The `str.maketrans()` function manufactures a translation table, and `translate()` uses it to replace each character in the string with the value specified in the translation table. This effectively converts the base of the number.