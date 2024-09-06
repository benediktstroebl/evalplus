```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product > 9:
        product = 0
    return product
```

The code directly addresses the problem statement by extracting the unit digits of both numbers using the modulo operation (`a % 10` and `b % 10`). These unit digits are then multiplied together to obtain a tentative product. Lastly, the function checks if the product is greater than 9, which would imply that the original numbers had digits greater than their unit places, and resets the product to 0 in such cases.

This approach ensures that the function considers only the unit places for multiplication and offers a clear and concise solution.