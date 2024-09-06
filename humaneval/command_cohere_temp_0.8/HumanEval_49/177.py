Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function accepts two integers as parameters, namely `n` and `p`. It utilizes the `pow` function to compute `2` raised to the power of `n` modulo `p`, adhering to the corresponding numeric constraints.