```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product > 9:
        product = product % 10
    return product
```

The function `multiply(a, b)` takes two integers `a` and `b` as arguments, extracts the unit digits of both numbers using the modulo operator (`%`), and then multiplies these unit digits. If the result of this multiplication is greater than 9, it means there's a two-digit number, so the function applies a second modulo operation to handle this case and returns the result. 

This solution is concise and adheres to the problem statement's assumptions about valid input. It avoids discussing edge cases that aren't relevant to the problem, such as negative numbers or values less than 10.