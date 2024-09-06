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
            res.append("i")

    return "".join(res)
```

This code defines a function int_to_mini_roman that takes a positive integer as input and converts it to its mini roman numeral representation as a string. It uses a loop to iterate through each digit of the integer and appends the appropriate roman numeral prefix to a result list. Finally, it joins the list to produce the roman numeral string.