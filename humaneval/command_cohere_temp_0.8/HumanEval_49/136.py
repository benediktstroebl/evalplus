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

This script includes a function `modp` that takes two integers `n` and `p` as input and returns the result of `2^n % p`. The function is defined in the module scope, and four test cases are provided to demonstrate its behavior. The tests cover different scenarios and confirm that the function behaves as expected. You can add more tests to further validate the function's behavior if needed.  This code can be included in a larger project, but if incorporated into a markdown cell it should be executed to demonstrate the behavior of the function.