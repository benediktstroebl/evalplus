```python
def modp(n, p):
    return pow(2, n, p)
```

This function `modp(n, p)` computes `2^n` modulo `p` using the built-in Python function `pow(x, y, p)`. This efficiently calculates the value of `x` raised to the power of `y` modulo `p` with minimal computational costs, ensuring that it optimally solves the problem.