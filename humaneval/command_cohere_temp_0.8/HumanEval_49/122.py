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

The function `modp` takes two integers `n` and `p` as input and returns `2^n modulo p` using the `pow` function and outputs the result modulo `p`. The tests demonstrate the behavior of the function for various test cases and ensure that it matches the problem statement. You can add more tests to cover a wide range of scenarios and validate the correctness of the function.  This solution benefits from Python's built-in exponentiation operator and the optimized modulo operation, resulting in a concise and efficient solution.  This solution is both self-contained and efficient.