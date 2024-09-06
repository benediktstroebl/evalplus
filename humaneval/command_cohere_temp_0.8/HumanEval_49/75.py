Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function accepts two integers as parameters, namely `n` and `p`. It then uses the `pow` function to calculate `2` raised to the power of `n` modulo `p`. This operation is useful in various mathematical and cryptographic applications, particularly for working with binary numbers or performing advanced arithmetic operations in modular environments.