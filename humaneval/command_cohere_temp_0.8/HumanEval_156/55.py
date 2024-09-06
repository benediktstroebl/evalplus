```python
def int_to_mini_roman(n):
    if n < 1:
        return ""

    res = []
    for i in range(1, 1000):
        if n >= i:
            num = str(i)
            roman = ROMAN_NUM[i]
            idx = len(roman) - 1
            while num > 0 and idx >= 0:
                res.append(roman[idx])
                num -= roman[idx]
                idx -= 1
            if num > 0:
                res.append(num)
            n -= i

    return ''.join(res)

ROMAN_NUM = {1: 'i', 5: 'v', 10: 'x', 50: 'l', 100: 'c', 500: 'd', 1000: 'm'}
```

This code block provides a Python script that tackles the problem of converting integers into mini roman numerals, within the specified range of 1 to 1000. The function `int_to_mini_roman` takes a positive integer as its argument and returns its corresponding roman numeral equivalent as a lowercase string. It employs a dictionary, `ROMAN_NUM`, which stores corresponding roman numerals for integers 1 to 1000. The function iterates through the given number, using each value to form the roman numeral, and any remaining digits will be added directly to the result. Finally, the function joins these roman numerals to form the final result.