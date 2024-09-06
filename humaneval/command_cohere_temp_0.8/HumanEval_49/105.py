Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function adheres to the problem statement, calculating 2^n modulo p using the built-in `pow` function and returning the result. It operates under the assumption that suitable numeric values are provided for 'n' and 'p.'  If you wish to further refine the function to incorporate explicit checks for invalid inputs or provide explicit handling of edge cases, please let me know so that I can offer suitable suggestions.

This function can be invoked with various test cases to evaluate its performance on different inputs:
```python
>>> modp(3, 5)
3
>>> modp(1101, 101)
2
>>> modp(0, 101)
1
>>> modp(3, 11)
8
>>> modp(100, 101)
1
```
This demonstrates its correct functionality for different scenarios.  If you want to enhance this function further in terms of input validation, error handling, or optimization, feel free to ask for guidance.