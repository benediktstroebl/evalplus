```python
def change_base(x, base):
    return str(x).translate(str.maketrans('123456789', f'{base}_{base}_{base}123456789'))
```

This approach utilizes the `str.translate()` method to replace characters with the corresponding base digits. For instance, when base = 2, '8' gets translated to '1000', and when base = 3, '7' becomes '111'. This method offers a straightforward solution without requiring any additional libraries.

The `change_base` function takes two parameters: `x`, the input number, and `base`, the desired base. It returns the numerical base of `x` converted to `base` as a string. The output corresponds to the string representation of the number, which may include characters like '1', '2', '10', etc., if the original number contains digits greater than the new base.