```python
def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by its coefficients. """
    result = [0] * (len(xs) - 1)
    x = 1
    for i in range(len(xs)):
        result[i] = xs[i] * x
        x *= 1
        x += 1
    return result
```

The test cases are included at the bottom of the script. When the script is executed, the tests are automatically run and verified against the expected outputs. 
```python
test_cases = [
    ([3, 1, 2, 4, 5], [1, 4, 12, 20]),
    ([1, 2, 3], [2, 6])
]

for coeffs, expected in test_cases:
    assert derivative(coeffs) == expected
```
If the output of the derivative function matches the expected output for each test case, the script will exit with 0, indicating successful execution. 

Any other exit code indicates that some or all tests failed. In that case, you will get a failure report for each test that failed.