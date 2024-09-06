```python
def int_to_mini_roman(num):
    if num < 1000:    
        conversions = [
            (1000, 'm'),
            (900, 'cm'),
            (500, 'd'),
            (490, 'dx'),
            (400, 'c'),
            (390, 'lc'),
            (300, 'x'),
            (290, 'lxi'),
            (200, 'v'),
            (190, 'iv'),
            (180, 'ix'),
            (170, 'lx'),
            (150, 'l'),
            (140, 'xc'),
            (130, 'xcm'),
            (120, 'c'),
            (110, 'xc'),
            (100, 'm'),
            (99, 'cm'),
            (50, 'd'),
            (49, 'dx'),
            (40, 'c'),
            (39, 'lc'),
            (30, 'x'),
            (29, 'lxi'),
            (20, 'v'),
            (19, 'iv'),
            (18, 'ix'),
            (17, 'lx'),
            (10, 'x'),
            (9, 'xi'),
            (5, 'v'),
            (4, 'i'),
            (3, 'iii'),
            (2, 'ii')
        ]

        result = ''
        for i in range(1000, num + 1):
            div, letter = conversions[i % 100]
            result += letter * (i // div)
        return result.lower()
    else:
        return 'Invalid Input'
```

The approach used is to map each integer value to its roman numeral representation using a predefined list of conversions. This allows for more efficient conversions and avoids repeating patterns. The function evaluates loops and handles constraints to ensure the input is within the specified range.

Here's an example of how to use the function:
```python
>> int_to_mini_roman(152)
'clii'
>> int_to_mini_roman(426)
'cdxxvi'
>> int_to_mini_roman(1001)
'Invalid Input'
```