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

The logic behind the code is to iterate over the roman_values list which stores the numerical values of each roman numeral. Then, for each value, we calculate the count of that particular roman numeral which is required to represent the given integer. Finally, we concatenate the relevant roman numerals together to form the answer.