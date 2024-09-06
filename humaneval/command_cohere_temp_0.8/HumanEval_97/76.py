```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product > 9:
        product = 0
    return product
```

The function `multiply(a, b)` takes two integers `a` and `b` as arguments, extracts the unit digits of both numbers using the modulo operation (`a % 10` and `b % 10`), and then multiplies these unit digits to obtain a candidate product. If the candidate product is greater than 9, it assumes that the product of the original numbers was zero, and therefore sets the product to zero to avoid an incorrect result.