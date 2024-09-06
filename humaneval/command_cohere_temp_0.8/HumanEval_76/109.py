```python
def is_simple_power(x, n):
    return type(x) is int and x == n ** int(n ** 0.5)
```
This function checks if a number `x` is a simple power of `n` by comparing it to the result of raising `n` to the power of the square root of `n` (which is the largest power of `n` that can produce `x`). The type check ensures that both inputs are integers, as the problem statement indicates.