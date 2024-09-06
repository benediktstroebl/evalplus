```python
def change_base(x, base):
    return str(x).translate(str.maketrans('123456789', f'{base}_{base}_{base}'))
```

This approach takes advantage of the `translate` method to change the digits of the number to the new base. For example, it translates the digits 1, 2, 3, 4, 5, 6, 7, 8, 9 to the new base by mapping them to `base` `base` `base`.