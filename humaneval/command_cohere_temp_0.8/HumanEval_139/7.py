Here's a Python script that defines the `brazilian_factorial` function, as per the problem statement:
```python
def special_factorial(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product
```

This function definition is encapsulated and independent, providing the `special_factorial` function to calculate the 'Brazilian factorial' based on the provided definition. The logic is straightforward, iterating through numbers from 1 to `n` and multiplying them to construct the product.