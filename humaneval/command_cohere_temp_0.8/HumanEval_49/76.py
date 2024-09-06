Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def modp(n, p):
    return pow(2, n, p)

# Tests
n_values = [3, 1101, 0, 3, 100]
p_values = [5, 101, 11, 101, 101]

for n, p in zip(n_values, p_values):
    assert modp(n, p) == eval(f'{2**n} % {p}')

print("All tests passed!")
```

The function `modp` computes `2^n` modulo `p` using the `pow` built-in function. The tests are defined by evaluating `2**n % p` for various values of `n` and `p` and comparing the result with the function's output.

This code demonstrates computing `2^n` modulo `p` for different values of `n` and `p` and ensures that the result matches the expected modulo operation.