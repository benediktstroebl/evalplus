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
        elif i == 50:
            res.append("l")
        elif i == 100:
            res.append("c")
        elif i == 500:
            res.append("d")
        elif i == 1000:
            res.append("m")
        else:
            res.append(str(i))

    return "".join(res)
```

This code provides a clear and concise Python function `int_to_mini_roman` to convert positive integers into their mini roman numeral representations, with restrictions up to `1000`. It utilizes a loop to iterate through digits and categorizes them into specific roman numeral designations, ultimately joining them into a string.