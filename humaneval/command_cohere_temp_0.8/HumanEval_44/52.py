```python
def change_base(x, base):
    return str(x).translate(str.maketrans('123456789', f'{base}_{base}_{base}123'))
```

This approach utilizes the `translate` method to replace digits with the corresponding base digits. For instance, when base=2, '8' gets replaced by '1000' since in base 2, '8' translates to '1000' in the dictionary created by `str.maketrans`. Similarly, `str.maketrans` creates a translation dictionary that considers the base and translates the number accordingly.

To further clarify, the `str.maketrans` method creates a translation table, mapping each character in `['1','2','3','4','5','6','7','8','9']` to the corresponding base digits (`base`, `base`, `base`, ...), which are then used to translate the decimal digits in the input number. This approach efficiently converts the base of the input number.