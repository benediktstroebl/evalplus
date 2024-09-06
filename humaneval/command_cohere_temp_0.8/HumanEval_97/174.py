```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product >= 10:
        product = product % 10
    return product
```

The code directly attacks the problem by extracting the last digit of each number (using the modulo operator (`%`) to always return the last digit) and then multiplying these extracted digits. The result is then modulated by 10 to ensure that if the product of two digits exceeds 10, it returns the expected single-digit product. 

For example, the call `multiply(148, 412)` returns `6` which is the product of the last digit of both numbers.