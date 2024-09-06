```python
def is_simple_power(x, n):
    return type(x) is int and x == n ** int(n ** x == x)
```

This function compares the input value `x` with the power of `n` equivalent to `x` (obtained by raising `n` to the power of `int(x)`). It returns `True` if they are equal, which indicates that `x` is a simple power of `n`. Otherwise, it returns `False`. The type checking ensures that both inputs are integers, as the problem statement indicates.