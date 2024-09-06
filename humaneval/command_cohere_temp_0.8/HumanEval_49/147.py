Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function defines the `modp` function which calculates `2^n` modulo `p` using the built-in `pow` function. The built-in `pow` function takes the base, the exponent, and the modulus as arguments and calculates the result of the exponentiation modulo the given modulus. It is a more efficient and shorter solution than implementing modular exponentiation from scratch. 
The `pow` function automatically takes care of the modular arithmetic calculations and handles cases like overflow or underflow that might arise when working with large numbers. 

Note that the assumption is that the reader has the required dependencies installed, like `markdown` for the code blocks and `pytest` for the unit tests.