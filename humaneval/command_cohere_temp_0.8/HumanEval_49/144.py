Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function accepts two integers as inputs, namely `n` and `p`, and returns `2` raised to the power of `n` modulo `p` using the `pow()` function.  Please note that the result will be a numerator if `p` is a prime number.