Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This script defines a function called `modp` that takes two integers `n` and `p` as input and returns `2^n modulo p` using the built-in Python `pow` function. 

To do this, the function uses the built-in Python `pow` function to compute the exponentiation, and then takes the result modulo `p`, as specified by the `mod` argument. This function simplifies the problem of calculating 2^n modulo p by expressing it in terms of a single exponentiation operation, leveraging Python's built-in math capabilities to handle the modular arithmetic.

To test this function, you can execute it with different input values in the console:
```python
modp(3, 5) # 3
modp(1101, 101) # 2
modp(0, 101) # 1
modp(3, 11) # 8
modp(100, 101) # 1
```
Each of these calls to `modp` returns the expected output from the original problem statement. 

This solution demonstrates how Python built-ins can provide both straightforward solutions and concise code for everyday programming problems.