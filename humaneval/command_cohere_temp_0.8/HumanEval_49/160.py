Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function adheres to the problem description provided in the code block. It efficiently calculates and returns 2^n modulo p using the built-in pow function, which automatically handles the modulo operation. This solution is both straightforward and optimized for the given task.