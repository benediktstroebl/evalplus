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

The `modp` function takes two integers `n` and `p` as input and returns `2^n modulo p` using the `pow` function and specializes in computing numeric expressions securely. The test suite demonstrates the function's behavior through a variety of scenarios confirming its correctness.  This solution provides a concise way to calculate the desired result while maintaining compliance with Python norms.  By thoroughly testing the function, you can guarantee that it fulfills the problem statement accurately and consistently.  Feel free to adapt and reuse this code in your projects, and let me know if you need anything else!