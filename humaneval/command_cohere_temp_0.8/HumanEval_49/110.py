```python
def modp(n, p):
    return pow(2, n, p)
```

This function takes two inputs, `n` and `p`, and returns `2` raised to the power of `n` modulo `p` using the `pow()` function. This handles the numerical intricacies, so you get the correct result automatically. 

This solution passes all the test cases provided in the original problem description.