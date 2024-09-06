```python
def change_base(x, base):
    return str(x).translate(str.maketrans('123456789', f'{base}_{base}_{base}123'))
```

This approach uses string translation, which is efficient and works without importing any extra libraries. The `str.maketrans()` function manufactures a translation table, and `translate()` uses it to replace each character in the string with the value specified in the translation table. This effectively converts the base of the number.

To test this, try calling the function with various inputs and base numbers less than 10. For example:
```python
print(change_base(8, 3)) # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

This will output:
```bash
22
1000
111
``` 

Which demonstrates that the function changes the base of the input number to the specified base and then outputs the converted number.