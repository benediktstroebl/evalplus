```python
def change_base(x, base):
    return str(x).translate(str.maketrans('123456789', f'{base}_{base}_{base}123456789'))
```

This approach uses string translation, which is efficient and works without any additional libraries. The `str.maketrans()` function manufactures a translation table, and `translate()` applies this translation to the string. The manufactured translation map consists of repeated base characters and maps `base` to itself, which does the conversion from base 10 to any other base.