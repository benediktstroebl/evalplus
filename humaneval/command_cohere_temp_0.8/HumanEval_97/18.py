```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product > 9:
        product = 0
    return product
```

The function `multiply(a, b)` takes two integers `a` and `b` as parameters. It extracts the unit digits of both numbers using the modulo operation (`modulo 10` for both `a` and `b`). These unit digits are then multiplied together to obtain a product. If the product is greater than 9, it means there is a carry-over, and the result is truncated to 0. The function then returns this product. 

This solution is self-contained and solves the problem as requested. It defines a single function that takes two integers and returns the product of their unit digits, as demonstrated in the example usage provided in the initial problem statement.