Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function adheres to the problem statement, calculating 2^n modulo p using the built-in `pow` function and returning the result. It does not rely on any external variables or assumptions beyond those expressed in the function signature.