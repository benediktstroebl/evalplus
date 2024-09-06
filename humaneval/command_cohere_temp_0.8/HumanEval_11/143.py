```python
def string_xor(a, b):
    return a.translate(str.maketrans('01','10')) == b.translate(str.maketrans('10','01'))
```

This approach performs XOR based on the translation table and the translation-based method. By using `str.translate()` with a translation table of `'01'` to `'10'`, it converts each `0` to `1` and each `1` to `0` effectively performing the binary XOR.

The condition checks `a.translate(...) == b.translate(...)` to determine if the result of the XOR operation is equal to the expected XOR'd string. This avoids appending the strings and uses a more efficient and concise approach.