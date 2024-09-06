```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product > 9:
        product = product % 10
    return product
```

The code directly computes the product of the unit digits and then performs modulo `10` to ensure the result is within the range of a single digit, as dictated by the problem statement.

This approach aligns with the problem's constraint of returning a single-digit product, as it considers only the units of the two numbers without any explicit repeated multiplication.