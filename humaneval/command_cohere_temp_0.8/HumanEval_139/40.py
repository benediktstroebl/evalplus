Here's a Python script that defines the `brazilian_factorial` function as described:
```python
def special_factorial(n):
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product

special_factorial(4)
```

The `special_factorial` function computes the `brazilian_factorial` of a given integer `n` as defined in the problem statement. It does this by multiplying all integers from 2 to `n` inclusive.