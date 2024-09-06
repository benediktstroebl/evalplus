Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return (1 << n) % p

# Tests
n, p = 3, 5
assert modp(n, p) == 3

n, p = 1101, 101
assert modp(n, p) == 2

n, p = 0, 101
assert modp(n, p) == 1

n, p = 3, 11
assert modp(n, p) == 8

n, p = 100, 101
assert modp(n, p) == 1
```

The `modp` function takes two arguments, `n` and `p`, and returns the result of `2` raised to the power of `n` modulo `p`. The tests demonstrate the function's behavior for various inputs and expected output. Adjust the values in the test suite to cover more scenarios if needed.