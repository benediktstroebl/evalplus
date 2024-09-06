Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def modp(n, p):
    return pow(2, n, p)

# Tests
assert modp(3, 5) == 3
assert modp(1101, 101) == 2
assert modp(0, 101) == 1
assert modp(3, 11) == 8
assert modp(100, 101) == 1
```

The `modp` function takes two integers `n` and `p` as input and returns `2^n modulo p` using the `pow` function and assumes the input is valid. 
Please note that the `pow` function in Python 3 automatically calculates the modulus when the third argument is omitted, hence the modulo is applied in this case. Ppow(2, n, p) calculates 2 raised to the power of n and then takes the result modulo p.  This is the typical way to calculate exponents in modular arithmetic.  The implementation is self-contained and does not rely on any external libraries or modules.  It also hasn't imported any modules in the code snippet you provided, so it's consistent with the given context.  However, please note that in a real-world scenario, you should ensure input validation and proper error handling to handle edge cases and ensure robustness.  This is left out here for the sake of simplicity.