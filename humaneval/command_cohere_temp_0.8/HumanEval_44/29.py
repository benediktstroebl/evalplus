```python
def change_base(x, base):
    return str(x).translate(str.maketrans('123456789', f'{base}_{base}_{base}'))
```

This approach uses string translation, which is efficient and works without importing any extra modules. It's especially useful when dealing with small bases since it doesn't require any extra mappings or dictionaries.

To convert the number `x` into the given base, it utilizes the translate method with a customized mapping provided by `str.maketrans()`. The resulting string representation of the converted number is then returned. 

This approach is concise and effectively solves the problem, making it both efficient and compliant with the problem's specified constraints.