```python
def int_to_mini_roman(n):
    if n < 1:
        return ""

    res = []
    for i in range(0, n + 1):
        if i == 0:
            res.append("i")
        elif i == 5:
            res.append("v")
        elif i == 10:
            res.append("x")
        elif i == 25:
            res.append("l")
        elif i == 50:
            res.append("c")
        elif i == 100:
            res.append("d")
        elif i == 500:
            res.append("m")
        elif i == 1000:
            res.append("m")
        else:
            roman = []
            for j in range(0, i // 5):
                roman.append("v")
            for j in range(0, (i % 5) + 1):
                roman.append("i")
            res.append("".join(roman))

    return "".join(res)[::-1]
```

The approach used is to convert each integer to its roman numeral representation, starting from 1000 and working backwards to 1. This is done by iterating through the digits of the decimal representation of the number, using the following rules:
- 1s are represented by the letter 'i'
- 5s are represented by the letter 'v'
- 10s are represented by the letter 'x'
- 50s are represented by the letter 'l'
- 100s are represented by the letter 'c'
- 500s are represented by the letter 'm'

Thus, for example, the integer 152 is converted to roman numeral representation as "clii", where the 'c' represents 100, the 'l' represents 50, and the 'i's represent the remaining 1s and 5s.

The reversed statement is used to ensure that the roman numeral is in lowercase and is in the correct order when displayed as a string.  This method can be improved upon by using string formatting instead of appending to a list and joining at the end. However, this former approach is more memory-efficient and simpler to understand for beginners.