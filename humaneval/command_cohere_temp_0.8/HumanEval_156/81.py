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
        elif n - i < 10 and i % 5 == 0:
            res.append("(")
            res.append(int_to_mini_roman(i // 5))
            res.append(")")
        elif n - i < 10:
            res.append(str(i))
    
    # Join and convert to lowercase
    roman_numeral = "".join(res).lower()
    return roman_numeral
```

The approach uses a recursive bottoms-up technique, which is more efficient and manageable compared to the conventional top-down approach. Notably, this solution does not need any import statements, making it self-contained. You can test the function by calling it with a few positive integers less than or equal to 1000 and comparing the output with the examples provided in the problem statement.