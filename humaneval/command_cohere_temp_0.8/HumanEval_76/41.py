```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

The given code directly tests the relationship between `x` and `n`. If `x` is the power of `n` (simple power), then it should be true, whereas if `x` is not a simple power of `n`, then it should be false.