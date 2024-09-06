```python
def modp(n, p):
    return pow(2, n, p)
```

This function `modp(n, p)` takes two integers 'n' and 'p' as inputs, and returns `2^n modulo p` using the `pow()` function. This function allows you to compute 2 raised to the power of 'n' and take the result modulo 'p', all in one step. It's a convenient way to perform these two common mathematical operations simultaneously without manual multiplication and modulo operations. 

This solution sets the exponent to 2 and the modulus to 'p', and the function returns the result of the computation modulo 'p'. 

Please note that the `pow()` function in Python 3 handles negative exponents differently, and as a result, some of the test cases provided, such as `modp(3, 5)` and `modp(3, 11)`, will return the same result as in the provided solution. 

If you are working with negative exponents, you may need to adjust your approach, such as using the expression `pow(2, n, p)` directly if you want to handle such cases separately. 

This function effectively solves the problem in a straightforward manner, conforming to the provided tests.  If you have particular scenarios in mind that involve negative exponents or other specific situations, feel free to elaborate on your requirements, and we can further refine the solution to best suit your needs.