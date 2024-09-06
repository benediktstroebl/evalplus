```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product > 9:
        product = 0
    return product
```

The function `multiply(a, b)` takes two integers `a` and `b` as parameters. It extracts the unit digits of both numbers using the modulo operation (`modulo 10`, which returns the last digit in the decimal representation). These unit digits are multiplied together to get the `product`. If the `product` is greater than 9, it increments the result to 0, handling the case where the original numbers have multiple digits beyond the unit digits. Ultimately, the function returns the product of the unit digits.