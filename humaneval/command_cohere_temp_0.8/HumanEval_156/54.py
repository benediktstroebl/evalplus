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
        elif n - i <= 400 and i % 100 in [50, 25, 10, 5, 0]:
            j = i % 100
            if j == 50:
                res.append("l")
            elif j == 25:
                res.append("x")
            elif j == 10:
                res.append("v")
            elif j == 5:
                res.append("i")
            elif j == 0:
                res.append("i")
        elif i % 500 == 0:
            m = i // 500
            res.append(f"{str(m)}m")
        else:
            res.append(f"{str(i)}x")

    return "".join(res)
```

The approach uses a nested loop to generate the roman numeral representation for `1 <= n <= 1000`. The generator uses the following rules:
- ``i`, ``v`, ``x`, ``l`, `c`, `d`, `m` for the respective decimal values.
- Certain numbers need to be split into multiple roman numerals, e.g., `152 -> clii`, `426 -> cdxxvi`, where `c` and `d` are used in their 1000's place to reflect their value.

The code leverages these rules and optimizes the output by minimizing the number of roman numerals used.