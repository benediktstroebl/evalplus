```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product > 9:
        product = 0
    return product
```

The function `multiply(a, b)` takes two integers `a` and `b` as arguments, extracts the unit digits of both numbers using the modulo operator (`%`), and then multiplies these unit digits to obtain a candidate result. If this candidate result is greater than 9, it indicates a two-digit number, and to ensure that the final result is a single digit, the product is reset to 0, and only the required unit digit is returned.