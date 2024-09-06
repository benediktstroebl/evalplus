```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = (dig1 * dig2) % 10
    return product
```

The function `multiply(a, b)` takes two integers a and b, extracts the unit digits of both numbers using the expression `a % 10` and `b % 10` respectively, and then multiplies these unit digits. The result is again reduced to its last digit and returned as the product of the unit digits. This solution is concise and adheres to the problem statement in the provided markdown code block. It assumes that the input is valid, as stipulated in the problem statement.