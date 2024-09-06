```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product >= 10:
        product = product % 10
    return product
```

The code directly calculates the product of the unit digits and then returns the result, ensuring it handles cases where the product of the unit digits is greater than 9. It is a straightforward solution that meets the problem requirements. 

If needed, I can also provide a more detailed explanation of any part of this code, or provide additional variants of the solution. Let me know if you have any further questions or comments on this response!