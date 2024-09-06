Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return (1 << n) % p

# Tests
assert modp(3, 5) == 3
assert modp(1101, 101) == 2
assert modp(0, 101) == 1
assert modp(3, 11) == 8
assert modp(100, 101) == 1
```

The function `modp` takes two integers `n` and `p` as input and returns the result of `2` raised to the power of `n` modulo `p`. The `assert` statements reinforce the function's expected behavior as outlined in the problem statement.