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
Please note that the assumption of input validity is important, as the function may encounter numerical issues with large numbers or when dealing with non-prime moduli. If valid inputs, the function will produce the expected results; otherwise, it may enter non-termination or produce incorrect outputs.  Output: | n | p | modp(n, p) |
|----|----|------------|
| 3 | 5 | 3 |
| 1101 | 101 | 2 |
| 0 | 101 | 1 |
| 3 | 11 | 8 |
| 100 | 101 | 1 |