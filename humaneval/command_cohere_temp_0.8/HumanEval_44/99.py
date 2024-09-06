```python
def change_base(x, base):
    return str(x).translate(str.maketrans('123456789', f'{base}{%d}' % base, base=base))
```

This approach utilizes the `translate` method to replace each digit `['0', '1', '2', ..., '9']` of the decimal number with the corresponding digit of the new base, specified as `f'{base}{%d}' % base`, resulting in the desired conversion.