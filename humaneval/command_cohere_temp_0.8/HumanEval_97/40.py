```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product > 9:
        product = product % 10
    return product
```

The code directly computes the product of the unit digits and then handles the case where the product is greater than 9, which requires consideration of two-digit numbers. This is a straightforward solution that efficiently solves the problem.