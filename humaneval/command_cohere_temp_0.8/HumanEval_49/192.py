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

The `modp` function takes two integers `n` and `p` as input and returns `2^n modulo p` using the `pow` function and selects the modulus accordingly.

The provided tests demonstrate the behavior of the function for various inputs and assert that the function output matches the expected output. 

  
```
Note that the pow function inherently takes two arguments, the base and the exponent, and the third optional argument exponentiates the modulus. 
```

This approach eliminates the need for extra variables and provides a concise solution to the problem.