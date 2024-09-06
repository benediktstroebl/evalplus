Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This script defines the `modp` function, which takes in two integers `n` and `p` as input and returns `2` raised to the power of `n` modulo `p` using the `pow` function. It assumes that the inputs are valid and will throw an error if the input values are invalid.