```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product >= 10:
        product = product % 10
    return product
```

The code directly calculates the product of the unit digits and then returns the result, ensuring compliance with the problem's specification.

This approach avoids complex conversions and instead provides a straightforward solution that elicits the desired behavior.