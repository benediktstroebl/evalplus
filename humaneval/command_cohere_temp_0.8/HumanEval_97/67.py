```python
def multiply(a, b):
    num_a = a % 10
    num_b = b % 10
    product = num_a * num_b
    if product > 9: 
        product = 0
    return product
```
The function extracts the unit digits of both numbers, multiplies them, and then checks if the resulting product is greater than 9. If so, it resets the product to 0 to ensure the final answer follows the constraint of only considering the unit digit.