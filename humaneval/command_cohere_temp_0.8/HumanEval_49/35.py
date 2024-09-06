Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function accepts two integers as inputs and returns the number 2 raised to the power of n, modulo p, using the built-in `pow` function and modulo operator (`%`).  This is an efficient implementation for the given problem.