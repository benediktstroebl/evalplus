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

The following expressions evaluate to true:
```python
>>> int_to_mini_roman(19) == 'xix'
True

>>> int_to_mini_roman(152) == 'clii'
True

>>> int_to_mini_roman(426) == 'cdxxvi'
True
```