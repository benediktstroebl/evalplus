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

This code defines a function `modp` that calculates `2^n % p` where `n` and `p` are input arguments, and provides test cases to validate its behavior.  This complies with the problem statement and corresponds to the provided example tests. If you would like to implement the function in a different manner, we can discuss alternative approaches. Please let me know if you have any questions or need further assistance with anything.