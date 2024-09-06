```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product >= 10:
        product = product % 10
    return product
```

The code directly leverages the modulo operator (`%`) to determine the unit digits of both numbers, before multiplying them and taking the result modulo 10 to ensure it remains within the range of 0 to 9. This approach efficiently computes the required result, ensuring correct handling of unit digits.