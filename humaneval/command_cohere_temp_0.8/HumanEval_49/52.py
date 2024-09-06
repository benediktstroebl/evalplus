Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function accepts two integers as parameters, namely `n` and `p`, and it returns `2` raised to the power of `n` modulo `p` using the Python operator `pow()`. 

To elaborate, the `pow()` function in Python performs numeric exponentiation, taking three arguments: the base (in this case, 2), the exponent (given by `n`), and the modulus (given by `p`). The function returns the result of `2` raised to the power of `n`, modulo `p`, as per the problem requirement. 

This solution employs the exponentiation-by-squaring technique, efficiently computing the result via iterative squaring, tailored to work modulo `p`. This method significantly reduces the number of multiplications and modulo operations required to compute the result compared to a straightforward recursive implementation. 

This solution is both efficient and concise, utilizing an inherent Python feature, the `pow()` function, to solve the problem. Notably, it only relies on standard Python functions and doesn't require any external libraries.