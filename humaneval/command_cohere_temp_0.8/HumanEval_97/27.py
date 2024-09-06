```python
def multiply(a, b):
    dig1 = a % 10
    dig2 = b % 10
    product = (dig1 * dig2) % 10
    return product
```

The code directly computes the product of the unit digits of `a` and `b` and returns the result. This is done using the modulo operation `%` to ensure that the result remains in the range of 0 to 9, representing the unit digit of the result. 

The code assumes and expects that the input is valid, as stated in the problem statement. It doesn't perform any additional validation or handling for edge cases beyond the specified input requirements. Make sure to provide the expected behavior for the code snippet if you want it to be tested according to the provided problem statement.