```python
def int_to_mini_roman(n):
    if n < 1:
        raise ValueError("Input must be a positive integer")

    roman = []
    while n > 0:
        number = str(n % 10)
        n = n // 10
        roman.append(ROMAN_VALS[number])

    roman = [str(i) for i in roman]
    mini_roman = ''
    for i in range(len(roman)):
        if i == 0:
            mini_roman += roman[i]
        elif roman[i] == 'i' and mini_roman[-1] != 'i':
            mini_roman += roman[i]
        elif roman[i] == 'v' and mini_roman[-1] != 'i' and mini_roman[-1] != 'v':
            mini_roman += roman[i]
        else:
            if roman[i] == mini_roman[-1]:
                mini_roman += roman[i]
            else:
                mini_roman += '{}{}'.format(roman[i], mini_roman[-1])
    return mini_roman

ROMAN_VALS = {
    'i': 'i',
    'v': 'v',
    'x': 'x',
    'l': 'l',
    'c': 'c',
    'd': 'cd',
    'm': 'cm',
}
```

This Python script defines a function `int_to_mini_roman` that converts an integer input to its miniature Roman numeral representation as a string. It validates the input being a positive integer and utilizes a dictionary `ROMAN_VALS` to map Arabic numerals to Roman numerals. The function iterates through the digits of the input, synthesizing the miniature Roman representation. It ensures the resulting string adheres to the specified format, favoring single-letter Roman numerals for compactness.