```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = (dig1 * dig2) % 10
    return product
```

The code directly computes the product of the unit digits, `dig1` and `dig2`, to obtain a fraction of the final result, `product`, and then returns it.

This approach avoids any unnecessary integer division and goes straight to the source to calculate the desired result, making it efficient and effective.