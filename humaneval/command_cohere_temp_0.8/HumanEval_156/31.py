```python
def int_to_mini_roman(num):
    roman_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_numerals = ['m', 'cm', 'd', 'cd', 'c', 'xc', 'l', 'xl', 'x', 'ix', 'v', 'iv', 'i']

    result = []
    for i in range(len(roman_values)):
        count = num // roman_values[i]
        result.extend(roman_numerals[i] * count)
        num %= roman_values[i]

    return ''.join(result)
```

The approach uses a list of roman numeral values and their corresponding digits, and a list of the mini roman numerals to map the integer input to the correct mini roman numeral representation.

To convert a number to mini roman numerals, the `int_to_mini_roman` function iterates over the `roman_values` list, each value representing the integer value of the roman numeral unit. It uses integer division to calculate how many times each unit is present in the input number. This ensures that larger values are prioritized over smaller ones. The `roman_numerals` list provides the lowercase characters used to form the roman numeral.

The resulting roman numeral digits are joined together to form the output string, with any remaining unused value handled by the modulo operation in the loop.