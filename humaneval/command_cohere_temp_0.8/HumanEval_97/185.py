```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product > 9:
        product = 0
    return product
```

The function `multiply(a, b)` takes two integers `a` and `b` as arguments, extracts the unit digits of both numbers using the modulo operator (`%`), and then multiplies these unit digits to obtain a candidate result. If the candidate result is more than 9, it is replaced with 0 to ensure the final result is a single-digit number. 

This approach handles edge cases such as "multiply(2020, 1851)" and "multiply(14, -15)" by effectively accounting for the units digit and returning 0 in cases where the product would be 10 or greater. 

The function then returns the simplified result.