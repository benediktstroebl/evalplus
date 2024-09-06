```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product > 9:
        product = product % 10
    return product
```

The function `multiply(a, b)` takes two integers `a` and `b` as arguments, extracts the unit digits of both numbers using the modulo operation (`dig1 = a % 10` and `dig2 = b % 10`), and then multiplies these unit digits to obtain a candidate product. If the candidate product is greater than 9, it's normalized to a single-digit number by taking its remainder when divided by 10, ensuring the final result conforms to the single-digit requirement. 

This solution adheres to the given requirement to return the product of the unit digits, assuming valid input, and handles the edge case of a multi-digit product to ensure it returns a single digit.