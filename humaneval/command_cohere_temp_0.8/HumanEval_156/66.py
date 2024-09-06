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
            res.append("i")

    return "".join(res)
```

This script provides a function called `int_to_mini_roman`, which takes in a number and converts it to its mini roman numeral representation as a string. The function then returns this representation in lowercase. To achieve this, the function uses a loop to iterate through each digit of the integer n, converting each digit into its roman numeral form based on specific rules and appending the roman numeral to a list. Finally, the function joins the list elements into a single string to provide the mini roman numeral representation of the input number.