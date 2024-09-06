```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = (dig1 * dig2) % 10
    return product
```

The function `multiply(a, b)` takes two integers `a` and `b` as parameters. It extracts the unit digits of both numbers using the modulo operation `% 10` to get `dig1` (unit digit of `a`) and `dig2` (unit digit of `b`). Then, it computes the product of these unit digits `dig1 * dig2` and mods the result by 10 to ensure it is also a unit digit, which is then assigned to `product`. Finally, it returns the `product`, which is the product of the unit digits of the two input numbers.

This approach eliminates the need for explicit integer division (`//`) and compares favorably with the naive approach in terms of code simplicity and efficiency.