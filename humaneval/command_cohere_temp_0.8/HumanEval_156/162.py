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

This code provides a clear and concise solution by using nested loops to iterate through numbers from 1 to 1000 and returning the appropriate Roman numeral characters for each range. The base cases consider the values that do not require repeating digits, such as 1, 5, 10, 25, 50, 100, 500, and 1000. The final result is joined into a string and returned as the Roman numeral representation of the input number.