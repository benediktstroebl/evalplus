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

The function `modp` takes two arguments: `n` represents the number to be shifted, and `p` represents the modulo denominator. It returns the result of shifting `n` times to the left and taking the remainder when divided by `p`. This is accomplished through the use of the binary shift operator `<<` and the modulo operator `%`.