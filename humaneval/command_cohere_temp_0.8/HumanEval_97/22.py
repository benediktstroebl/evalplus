```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = dig1 * dig2
    if product > 9:
        product = 0
    return product
```

The code directly computes the product of the unit digits and then trims the result to a single digit by toggling over 9 and resetting to 0. 

This approach allows the code to fulfill the requirements of the problem in a straightforward and efficient manner. And the unit testing framework allows the verification of the correctness of the code against expected values.