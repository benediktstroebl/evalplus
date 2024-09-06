```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = (dig1 * dig2) % 10
    return product
```

The code directly computes the product of the unit digits of `a` and `b` and returns the result, achieving the goal in a straightforward manner while maintaining efficiency and readability.

This approach avoids complex intermediate calculations and utilizes the modulo operation to ensure the result remains within the 1-9 range of unit digits.