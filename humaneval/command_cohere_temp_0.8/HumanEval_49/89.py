```python
def modp(n, p):
    return pow(2, n, p)
```

This function `modp(n, p)` computes `2^n % p` by leveraging the built-in function `pow(x, y, p)`, which calculates `x^y % p` efficiently. The result is the desired exponentiation `2^n % p`, ready for use in various cryptographic and mathematical applications, including creating cryptographic keys, working with finite fields, and solving modular equations. 

This approach improves code readability and efficiency, making it a recommended way to perform modular exponentiation in Python. 

Note: Python uses the `mod` keyword for module deprecation, so we use the more descriptive `modp` name instead.