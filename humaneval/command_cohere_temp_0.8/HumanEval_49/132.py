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

The function 'modp' computes `2^n` modulo `p` using the built-in Python function 'pow' and appropriately handles the numeric cases mentioned in the prompt.

The test suite includes a variety of situations highlighted in the prompt to verify that the function delivers the appropriate results.