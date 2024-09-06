```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product > 9:
        product = product % 10
    return product
```

The function `multiply(a, b)` takes two integers a and b as input, extracts the unit digits of both numbers using the modulo operation (`dig1 = a % 10` and `dig2 = b % 10`), and then multiplies these unit digits (`product = dig1 * dig2`). If the result is greater than 9, it means there is a carry-over, so we apply the modulo operation again to ensure the final result is in the range of 0 to 9 (`if product > 9: product = product % 10`). 

This way, the function computes the product of the unit digits, considering any carry-over, and returns the result as the output.