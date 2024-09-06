```python
def modp(n, p):
    return pow(2, n, p)
```

This function `modp(n, p)` computes `2^n % p` by leveraging the built-in function `pow()`. This is a more efficient approach compared to manually implementing the algorithm from scratch, especially for larger values of `n` and `p`. 

Please note that the function assumes the inputs `n` and `p` to be integers. If any non-integer values are passed, the behavior would not be as expected.