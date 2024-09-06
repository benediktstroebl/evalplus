```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product > 9:
        product = 0
    return product
```

The function `multiply(a, b)` takes two integers `a` and `b` as parameters. It extracts the unit digits of both numbers using the modulo operation (`a % 10` and `b % 10`). These unit digits are then multiplied together to get the `product`. If the `product` is greater than 9, it indicates that the original numbers had a digit greater than 9 in their units place, and to get the actual product, we reset the `product` to 0.

This solution adheres to the problem statement and assumes that the input is valid, as specified in the provided function specification.