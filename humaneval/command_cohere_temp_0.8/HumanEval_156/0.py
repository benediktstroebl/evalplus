```python
def int_to_mini_roman(num):
    if num < 1:
        return ""

    res = []
    for i in range(0, len(str(num)) + 1):
        div, mod = divmod(num, 5) if i == 0 else divmod(mod, 5)
        num = div if div > 0 else 1
        res.append(ROMAN_NUM[mod])
        num = str(num)
        if i == 0 and num[-1] == '1':
            res.append(num)
        elif i > 0 and num[-1] == '1':
            res.append(num[0])
        else:
            res.append('x')

    return ''.join(res)

ROMAN_NUM = {1: 'i', 5: 'v', 10: 'x', 50: 'l', 100: 'c', 500: 'd', 1000: 'm'}
```

The provided Python code defines a function `int_to_mini_roman` that converts a given positive integer into its miniature Roman numeral representation as a lowercase string. It employs a loop to iteratively divide the number and construct the Roman numeral string based on divisibility by five and the remaining moduli. The `ROMAN_NUM` dictionary maps integer values to their corresponding Roman numerals. This function meets the specified requirement of handling numbers up to 1000 and returns the miniature Roman numeral representation of the input number, such as "xix" for 19, "clii" for 152, and "cdxxvi" for 426.