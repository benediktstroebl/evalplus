Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function defines the `modp` function which calculates `2^n % p` directly using the built-in `pow` function with the modulo operator. This avoids any issues with numerics and directly computes the result. It is a concise and efficient solution.