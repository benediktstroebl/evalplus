```python
def modp(n, p):
    return pow(2, n, p)
```

This function `modp(n, p)` takes two integers `n` and `p` as input, returns the value of 2 raised to the power of `n` and then takes the result modulo `p`. This is accomplished by using the built-in Python function `pow(x, y, p)`, which raises `x` to the power of `y` and returns the result modulo `p` when a third argument is passed in. This is a direct implementation of the specification provided in the prompt.