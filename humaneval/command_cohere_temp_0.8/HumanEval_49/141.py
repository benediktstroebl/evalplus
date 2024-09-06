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

The function `modp` takes two integers `n` and `p` as input and returns `2^n modulo p` using the `pow` function and outputs the result modulo `p`. 

The test suite demonstrates the function's behavior for a variety of inputs and asserts that the function's output matches the expected output for each test case.  This behaves as described in the problem statement.  It is also worth noting that, in practice, you should be cautious about the floating-point semantics of `pow(2, n)`, as well as any issues related to numerical overflow or underflow.  This is mentioned in the original problem statement.  However, the provided script will still solve the equation for a wide range of inputs.