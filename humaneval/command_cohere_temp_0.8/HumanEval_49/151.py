Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function accepts two integers as inputs and returns the number 2 raised to the power of n, modulo p. Both inputs are immediately utilized in the function; no additional or stored variables are required. The function fulfills the challenge statement without them having any external influence on the execution.