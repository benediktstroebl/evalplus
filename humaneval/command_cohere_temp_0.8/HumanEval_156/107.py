```python
def int_to_mini_roman(n):
    if n < 1:
        return ""
    
    res = []
    for i in range(0, len(n)):
        num = n[i]
        if num == 0:
            continue
        num = str(num)
        if num.endswith("1"):
            res.append(num[:-1])
        elif num.endswith("2"):
            res.append(num[:-1] + "i")
        elif num.endswith("3"):
            res.append(num[:-1] + "ii")
        elif num.endswith("4") or num.endswith("6") or num.endswith("8"):
            res.append(num[:-1] + "iv")
        elif num.endswith("5") or num.endswith("7") or num.endswith("9"):
            res.append(num[:-1] + "v")
        elif num.endswith("0"):
            res.append(num[:-1] + "x")
        else:
            res.append(num)
    
    return "".join(res)
```

This script provides a function `int_to_mini_roman` that converts a given positive integer to its roman numeral equivalent as a string with lowercase letters. It iterates through each digit of the passed number and appends the appropriate roman numeral letter to the result array, using specific conditions for each digit. Finally, the function returns the joined result array as a roman numeral-formatted string.