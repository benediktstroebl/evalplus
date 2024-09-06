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

This code defines a function `modp` that calculates `2^n % p` using bit shifting and modular arithmetic, ensuring the result fits within the range of `p`. The tests verify the function's behavior against various inputs.