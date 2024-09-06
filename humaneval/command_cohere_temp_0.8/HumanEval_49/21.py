```python
def modp(n, p):
    return pow(2, n, p)
```

This function takes two inputs, `n` and `p`, and returns `2` raised to the power of `n` modulo `p` using the `pow()` function. This is a direct implementation of the problem statement, without any improvements or optimizations. 

This solution is concise and straightforward, but it may not be the most efficient for large numbers or certain values of `n` and `p`. As mentioned, it does not have any relevant optimizations, nor does it handle potential issues like numeric overflow or edge cases. Nevertheless, it correctly solves the problem as stated.