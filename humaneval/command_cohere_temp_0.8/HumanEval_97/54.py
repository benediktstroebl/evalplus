```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product > 9:
        product = product % 10
    return product
```

The code directly computes the product of the unit digits and then handles the case where the product is greater than 9, which requires further adjustment to ensure the final result is in the range of 0 to 9. 

To validate the behavior of the code, we can write a test suite containing examples from the problem statement. 

This solution does not require any additional libraries. It uses Python's modulo operator (`%`) to obtain the unit digit and performs the necessary calculations directly, ensuring it computes the described behavior of the unit digit product.