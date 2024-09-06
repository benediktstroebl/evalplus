```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product >= 10:
        product = product % 10
    return product
```

The code directly multiplies the unit digits (`dig1 % 10` and `dig2 % 10`) to get the product. If the result is larger than 9, it applies a modulo operation to ensure the answer corresponds to the unit digit of the product. This way, the code efficiently computes the product of unit digits, ensuring the result fits within a single digit.