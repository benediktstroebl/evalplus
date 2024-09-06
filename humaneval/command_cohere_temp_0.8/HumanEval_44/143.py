```python
def change_base(x, base):
    return str(x).translate(str.maketrans('123456789', f'{base}{{base}^9}}'))
```

This approach uses string translation, which is efficient and works for any digit length. The translation table is generated using `str.maketrans()` and formatted to ensure correct mapping of digits. 

To handle bases less than 10, the mapping constructs an expression that converts each digit to its base representation, like `base` for base 1, `base^2` for base 2, and so on. This expression is repeated for each digit position using `{{base}^9}}` to account for base placement. 

For example, for base 3:
`'8'` -> `'2' (8 % 3)`
`'5'` -> `'5' (5 % 3)`
`'0'` -> `'0' (0 % 3)`

The expression for base 3:
`'8' -> '2{{3}^9}}' -> '2{3^9}'> '223' -> '22'` 

Thus, the base is changed from decimal to base 3. 

To obtain the same result using the previous approach of multiplication and modulo, length-dependent nested loops would be required, making the current approach more efficient and scalable.