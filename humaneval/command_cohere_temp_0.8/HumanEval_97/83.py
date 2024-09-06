```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = (dig1 * dig2) % 10
    return product
```

The code directly computes the product of the unit digits of `a` and `b` and returns the result. This is done using the modulo operator `%` to ensure that the result remains in the range of 0 to 9, representing the unit digit of the product. 

The function adheres to the problem's assumption that the input is valid, as it assumes the input is an integer that may not be entirely positive or negative. It appropriately addresses the mentioned test cases, including positive and negative integers and scenarios with and without non-zero unit digits.