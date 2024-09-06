```python
def modp(n, p):
    return pow(2, n, p)
```

This function `modp(n, p)` computes `2^n` modulo `p` using the built-in function `pow(x, y, p)`. This efficiently calculates the result of raising `x` to the power of `y` modulo `p` using the modular exponentiation algorithm. The function elegantly handles the exponential growth of `2^n` by computing the result modulo `p`, ensuring that the intermediate values never grow too large to cause computational challenges, as long as `p` is not a trivial prime number.

This solution is concise and leverages Python's built-in optimizations for modular exponentiation, making it an efficient approach for this problem. The function fully adheres to the problem description provided in the markdown code block.