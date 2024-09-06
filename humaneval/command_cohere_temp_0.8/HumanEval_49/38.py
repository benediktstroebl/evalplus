Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def modp(n, p):
    return pow(2, n, p)

# Tests
n_values = [3, 1101, 0, 3, 100]
p_values = [5, 101, 11, 101, 101]

for n, p in zip(n_values, p_values):
    assert modp(n, p) == eval(f'{2**n} % {p}')
```

The function `modp` computes `2^n` modulo `p` using the built-in Python function `pow` and returns the result. The tests are comprised of pairs of values where the first element is the 'n' value, and the second is the 'p' value; the assert statement checks if the result of the function corresponds to the manual calculation. 

For example, the first test case checks `modp(3, 5)`, and asserts that the function's result corresponds to the manual calculation of `2**3 % 5` which equals 3. 

This solution is straightforward and effective, but it may be worth noting that the `pow` function tends to be more efficient for large numbers.  Ultimately, this approach provides an optimal solution, sacrificing sophistication for simplicity and efficiency.