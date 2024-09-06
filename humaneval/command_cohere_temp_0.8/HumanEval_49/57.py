Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function defines the modp function which calculates 2^n modulo p. It uses the built-in Python function pow() which returns x to the power of y modulo m. In this case, it calculates 2 to the power of n modulo p.  For example, if n = 3 and p = 5, the function will return 3 as follows:
```python
>>> modp(3, 5)
3
```
This solution is self-contained and does not require any external modules or imports. It also has a concise one-line solution.