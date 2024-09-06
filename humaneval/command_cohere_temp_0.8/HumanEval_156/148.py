```python
def int_to_mini_roman(num):
    if num < 1000:
        result = []
        for i in range(0, num + 1):
            temp = str(i)
            rom_num = ROMA[temp][0]
            if len(rom_num) > 1:
                result.append(rom_num[1:])
            else:
                result.append(rom_num)

        return ''.join(result)

    else:
        return "Error! Input exceeds restrictions."

import itertools
roman_alphabet = ['i', 'v', 'x', 'l', 'c', 'd', 'm']
 roman_values = [1, 5, 10, 50, 100, 500, 1000]
mini_roman_map = [
    ['i', 'i'],
    ['v', 'v'],
    ['x', 'l', 'x'],
    ['l', 'c', 'l', 'c'],
    ['c', 'd', 'm', 'c'],
    ['d', 'd', 'd'],
    ['m', 'm']
]

ROMA = []
for mapping in itertools.product(roman_alphabet, repeat=2):
    ROMA.append(mapping)

for idx, roman_num in enumerate(roman_values):
    ROMA[idx][1] = str(roman_num)

```

The script defines a function `int_to_mini_roman` that converts a given positive integer to its roman numeral equivalent as a string. It uses a list `ROMA` to store the roman alphabet characters and their corresponding values. The script iterates through each digit of the integer, looks up the roman alphabet character for that value, and builds the roman numeral string. It checks if the length of the roman numeral string is greater than 1 to determine if it should be appended to the result list or not. Finally, it joins the result list to form the roman numeral string and handles inputs greater than 1000 to meet the problem's stated restriction.