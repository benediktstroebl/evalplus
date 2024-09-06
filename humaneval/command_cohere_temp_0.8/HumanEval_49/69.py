```python
def modp(n, p):
    return pow(2, n, p)
```

This function `modp(n, p)` takes two integers 'n' and 'p' as inputs, and returns `2^n modulo p`. This is accomplished via the built-in Python function `pow(x, y, p)`, which computes the value of `x` raised to the power of `y` modulo `p`, as described in the docstring of the built-in Python function `pow`. 

The function is self-contained, meaning it does not rely on any external variables or functions other than those explicitly given in the parameter list. It is a standalone function that can be copied and pasted into a Python environment and run without errors, as long as the variables 'n' and 'p' are provided when calling the function.