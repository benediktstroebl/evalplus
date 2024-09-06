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

The `modp` function takes two integers `n` and `p` as input and returns `2^n % p`, the remainder of the division of `2^n` by `p`. 

The tests are provided to demonstrate the function's behavior on different inputs. You can optionally add additional tests to cover more scenarios and ensure the correctness of the function.