Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def modp(n, p):
    return pow(2, n, p)

# Tests
n_values = [3, 1101, 0, 3, 100]
p_values = [5, 101, 11, 101, 101]

for n, p in zip(n_values, p_values):
    assert modp(n, p) == eval(f'{2**n % p}')

print("All tests passed!")
```

The function 'modp' computes `2^n modulo p` using the 'pow' function, which is a built-in Python function for exponentiation and modular arithmetic. The `eval` function is used to test the function 'modp' with numerical examples. The tests are defined by the pairs of values 'n_values' and 'p_values'. The test validates that the output of the function under test corresponds to the result of evaluating the expression `2**n % p`. 

The output of this code will be:
```
All tests passed!
```