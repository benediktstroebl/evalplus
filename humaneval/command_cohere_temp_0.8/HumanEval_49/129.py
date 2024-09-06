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

The `modp` function takes two integers `n` and `p` as input and returns `2^n modulo p` using the `pow` function and ignores numerical issues. The test suite demonstrates the function's behavior with various inputs and asserts the expected output.