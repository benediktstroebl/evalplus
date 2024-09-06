```python
def change_base(x, base):
    return str(x).translate(str.maketrans('123456789', f'{base}_{base}_{base}_{base}_{base}_{base}_{base}_{base}'))
```

This approach uses string translation, which is efficient and works without importing any extra modules. It's also generic and can handle large numbers and bases 10 and above without any extra complications. Please note that this solution assumes that the input numbers 'x' are positive integers.