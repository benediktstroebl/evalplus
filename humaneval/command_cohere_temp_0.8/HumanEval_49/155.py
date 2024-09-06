```python
def modp(n, p):
    return pow(2, n, p)
```

This function `modp(n, p)` computes `2^n` modulo `p` using the built-in Python function `pow(x, y, p)`, which works efficiently for any base `x` and exponent `y`, especially when `p` is large. 

It's a concise and optimized solution, especially for larger exponents and moduli, as it leverages built-in functions designed for such computations. 

When you need to compute other exponentiations or moduli, you can readily adapt this function, since it operates generically on the arguments `n` and `p`. 

This approach is commonly used in practice, as it balances readability, efficiency, and flexibility, making it a preferred solution for scenarios involving exponentiation and modular reduction. 

If you have additional problems or test cases like 'n == 1101 and p == 101', 'n == 0 and p == 101', or 'n == 3 and p == 11' that you'd like to verify using this function, feel free to incorporate them into your tests.