```python
def int_to_mini_roman(num):
    roman_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_numerals = ['m', 'cm', 'd', 'cd', 'c', 'xc', 'l', 'xl', 'x', 'ix', 'v', 'iv', 'i']
    
    result = []
    for i in range(len(roman_values)):
        while num >= roman_values[i]:
            num -= roman_values[i]
            result.append(roman_numerals[i])
            
    return ''.join(result)
```

The Python script defines a function, `int_to_mini_roman`, which converts a given positive integer into its mini Roman numeral representation as a string. It utilizes two lists: `roman_values` contains the corresponding Roman numerals for each integer value from 1 to 1000, and `roman_numerals` contains the mini Roman numerals.

The function iterates through the `roman_values` list, using a while loop to repeatedly subtract the largest Roman value less than or equal to the remaining number. This ensures the resulting Roman representation is mini by using the smallest possible Roman numerals. It then joins the miniature Roman numerals to form the final string representation of the Roman numeral.