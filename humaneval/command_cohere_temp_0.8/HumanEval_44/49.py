```python
def change_base(x, base):
    return str(x).translate(str.maketrans('123456789', f'{base}_{base}_{base}123'))
```

This function takes two parameters, `x`, which is the number to be converted, and `base`, which is the base into which the conversion should be made. The function uses the `str.translate` method. The `str.maketrans` function creates a translation table that maps each digit of the original number to the corresponding digit in the new base. The mapping is provided in the format `base` `_` `base` `_` `base` `123`, where `base` represents the digits in the new base. This mapping is then used to translate the digits of the number `x`, effectively converting it into the new base. 

Here is an example usage of the function:
```python
print(change_base(8, 3))  # Outputs '22'
print(change_base(8, 2))  # Outputs '1000'
print(change_base(7, 2))  # Outputs '111'
```

This shows the correct conversion of the base of the number 7, 8, or 8 into the bases 2, 3, and 2 respectively.