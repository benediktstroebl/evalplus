```python
def int_to_mini_roman(num):
    roman_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_numerals = ['m', 'cm', 'd', 'cd', 'c', 'xc', 'l', 'xl', 'x', 'ix', 'v', 'iv', 'i']
    
    result = []
    for i in range(len(roman_values)):
        count = num // roman_values[i]
        result.extend(roman_numerals[i] * count)
        num %= roman_values[i]
    
    return ''.join(result).lower()
```

The logic behind the code is to iterate over the roman values and use the modulo operator to perform the corresponding operation. Finally, the script joins the list of roman numerals into a string and converts it to lowercase.