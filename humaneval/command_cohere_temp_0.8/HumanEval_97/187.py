```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product > 9:
        product = product % 10
    return product
```

The function `multiply(a, b)` takes two integers `a` and `b` as arguments, extracts the unit digits of both numbers using the modulo operator (`%`), and then multiplies these unit digits. If the result of this multiplication is greater than 9, it implies that the original numbers had more than one digit, and the result would wrap around to a single-digit number. In this case, we apply the modulo operation again to ensure the result is a single digit.

This solution assumes that the input is valid and will not throw any exceptions, as per the assumption stated in the problem statement.