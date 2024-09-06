```python
def change_base(x, base):
    return str(x).translate(str.maketrans('123456789', f'{base}_{base}_{base}123'))
```

This approach utilizes string translation with translation strings formed from the specified base and numeric digits. This allows for quick and intuitive conversion.

The `translate` method is used in Python to replace specified characters with specified strings. The `str.maketrans` function creates a translation map that maps each of the digits '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' to the specified string `base` repeated twice, and then joined with a '_' to achieve the base conversion. This technique provides an elegant and efficient solution.