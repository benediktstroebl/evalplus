Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function defines the `modp` function which takes in two integers `n` and `p` and returns `2^n modulo p` using the `pow()` function.  The `pow(x, y, m)` function returns `x` raised to the power `y` modulo `m` while taking care of numeric overflow automatically.