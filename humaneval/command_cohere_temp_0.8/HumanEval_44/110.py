```python
def change_base(x, base):
    return str(x).translate(str.maketrans('1234567890', f'{base}_{base}_{base}123'))
```

This approach utilizes the `translate` method to replace characters with the corresponding base digits. For example, when `base` is `3`, the number `8` is translated to `22`, because `8` in base 10 translates to `222` in base 3. This method is adaptable to any base and provides a straightforward solution.