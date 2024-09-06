Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function uses the `pow` function to compute `2` to the power of `n` modulo `p`. It's a more efficient and streamlined way to accomplish the task compared to manual iterative or exponentiation methods.