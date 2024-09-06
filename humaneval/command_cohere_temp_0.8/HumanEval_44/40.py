```python
def change_base(x, base):
    return str(x).translate(str.maketrans('123456789', f'{base}_{base}_{base}123'))
```

This function takes two inputs: `x`, which is an integer, and `base`, which is the base of the numerical conversion. Using the translation table created with `str.maketrans`, the function converts the digits of `x` to the new base, ensuring `base` is less than 10 to comply with the problem statement's requirement. The resulting string representation of the converted number is returned. 

To perform the conversion correctly, ensure that you install the required package `string`:
```bash
pip install string
``` 

This package is necessary to utilise the `str.maketrans` function for translation.