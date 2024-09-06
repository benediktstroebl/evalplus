Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function accepts two integers as inputs, namely `n` and `p`, and returns `2` raised to the power of `n` modulo `p` using the Python operator `pow()`. 

This aligns with the problem statement and the provided tests, as the function correctly calculates `2` raised to the power of `n` modulo `p`. 

To operate successfully, the `pow()` function requires an explicit second argument: the modulus `p`. This is defined by the `%` mathematical operation.