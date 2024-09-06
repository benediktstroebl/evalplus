```python
def int_to_mini_roman(num):
    roman_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_numerals = ['m', 'cm', 'd', 'cd', 'c', 'xc', 'l', 'xl', 'x', 'ix', 'v', 'iv', 'i']
    
    result = []
    for i in range(len(roman_values)):
        while num >= roman_values[i]:
            num -= roman_values[i]
            result.append(roman_numerals[i])
    
    return ''.join(result).lower()
```

The logic behind the code is to iterate over the roman numeral values and iterate until the current value is bigger than the remainder of the division of the number by the current roman numeral value. The function works correctly as described in the prompt.