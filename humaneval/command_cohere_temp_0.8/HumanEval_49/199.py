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

The function `modp` takes two integers `n` and `p` as input and returns `2^n modulo p` using the `pow` function and expects the caller to be aware of numeric issues like overflow, underflow, and modulo numerics. 

The tests demonstrate the function's behavior for various test cases and ensure that it produces the expected results.  This code assumes that the `pow` function handles the exponentiation and modulo operations correctly, which is generally true for built-in Python functions on common platforms. 

Please be aware of potential numeric issues when using this function with very large or small numbers, as well as different numeric representations (e.g., floating-point vs. integer types).  If you need to handle extreme cases or require additional numeric safeguards, further modifications might be necessary.