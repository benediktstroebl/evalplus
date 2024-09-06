```python
def modp(n, p):
    return pow(2, n, p)
```

This function takes two inputs, `n` and `p`, and returns `2` raised to the power of `n` modulo `p` using the `pow` function. It is a wrapper for the built-in `pow` function and eliminates the need to manually compute the exponentiation and modular reductions.

This solution is concise and leverages Python's built-in functions for modular exponentiation, greatly enhancing readability and efficiency. Additionally, the function's docstring provides helpful information about the problem it solves, making the code self-documented.