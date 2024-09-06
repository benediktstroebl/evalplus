```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product > 9:
        product = product % 10
    return product
```

The function `multiply(a, b)` takes two integers a and b as input, extracts the unit digits of both numbers using the expression `a % 10` and `b % 10` respectively, and then calculates the product of these unit digits. Finally, it returns the result.

This approach assumes that the input numbers are valid and properly formed integers. Even if the input is not truly integers, the function will return incorrect results. If you want to handle such cases, you must add thorough input validation and error handling.