```python
def change_base(x, base):
    return str(x).translate(str.maketrans('123456789', f'{base}_{base}_{base}123'))
```

This approach utilizes the `str.translate()` method to convert numbers from the base `10` to any other base less than `10`. Numbers like `8` in base 10 would be converted to base 3 as:
```
8 -> "8" -> "8" -> "22" in base 3.
```

The `str.maketrans()` function is used to create a translation table that maps digits `0-9` to the corresponding digits in the new base. The resulting string is then converted to an integer using `int()` and returned.

To handle numbers larger than `9` in the input, the `translate()` method combines the translation of the `1`s` digit with the translation of the `0`s` digit. For example, `18` in base 10 would be converted to base 3 as:
```
18 -> "18" -> "18" -> "122" in base 3.
```

This approach minimizes the number of digits translations and thus improves performance.