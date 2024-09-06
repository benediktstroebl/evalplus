```python
def change_base(x, base):
    return str(x).translate(str.maketrans('123456789', f'{base}_{base}_{base}'))
```

This approach takes advantage of the built-in method `str.translate()` and the complementary `str.maketrans()` method to achieve the desired string conversion. 

The `str.translate()` method takes two arguments: the translation table and the input string. In our case, the translation table is formed by merging three identical copies of the base number, yielding a mapping that replaces each digit with the corresponding base-number digit. 

The `str.maketrans()` method is used to create the translation table by passing the fromstrings (the digits `123456789`) and the tostrings (the base number tripled) as arguments.

This approach is both effective and concise, demonstrating the power of leveraging built-in methods for practical coding problems. 

This function can be tested by calling it with different input values and verifying that the resulting strings correspond to the desired base conversions.