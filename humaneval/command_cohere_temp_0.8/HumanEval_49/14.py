```python
def modp(n, p):
    return pow(2, n, p)
```

This function `modp(n, p)` computes `2` raised to the power of `n` and then takes the result modulo `p`. It essentially answers the question, "What is 2 to the power of n, modulo p?" The Python built-in function `pow(x, y, m)` returns `x` raised to the power of `y` modulo `m`, which simplifies the code directly without any additional variables or calculations needed.