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

The `modp` function takes two integers `n` and `p` as input and returns `2^n modulo p` using the `pow` function and modifies the result to be relative to `p`. The test suite provides a variety of inputs and expected outputs to confirm the correctness of the function.

By providing a solution in a test-driven manner, this response not only solves the problem but also validates its correctness through the included tests. Feel free to modify the tests or add more scenarios to thoroughly validate the solution according to your requirements.