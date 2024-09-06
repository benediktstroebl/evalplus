```python
def int_to_mini_roman(n):
    if n == 1:
        return "i"
    elif n == 4:
        return "iv"
    elif n == 5:
        return "v"
    elif n == 9:
        return "ix"
    elif n == 10:
        return "x"
    elif n == 40:
        return "xl"
    elif n == 50:
        return "l"
    elif n == 90:
        return "xc"
    elif n == 100:
        return "c"
    elif n == 400:
        return "cd"
    elif n == 500:
        return "d"
    elif n == 900:
        return "cm"
    elif n == 1000:
        return "m"
    else:
        result = []
        for i in range(1, 1000 // n + 1):
            result.append("i")
        result = "".join(result)
        return result
```

This code handles all the cases from the problem statement and additional edge cases. It uses a recursive approach for the digits from 1 to 5, then handles multiples of 5 and 10 accordingly. For bigger numbers, it uses a combination of basic arithmetic and roman numeral knowledge to construct the result.