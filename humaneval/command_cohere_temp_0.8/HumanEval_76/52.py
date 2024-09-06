```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n * n)
```

This function evaluates to true when `x` is a simple power of `n` i.e. `x == n**int(x == n*n)`. The int check is necessary to catch non-integer powers, the equality checks are needed to handle the cases n**int=x and n**(int(n*n))=x correctly.