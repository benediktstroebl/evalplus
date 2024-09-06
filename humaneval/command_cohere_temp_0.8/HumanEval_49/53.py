Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function defines the `modp` function, which takes in two integers `n` and `p` as input and returns `2` raised to the power of `n` modulo `p` using the `pow` function. This agrees with the provided behavior for the test cases ">>> modp(3, 5) = 3", ">>> modp(1101, 101) = 2", ">>> modp(0, 101) = 1", ">>> modp(3, 11) = 8", and ">>> modp(100, 101) = 1".  This code also passes the provided tests.