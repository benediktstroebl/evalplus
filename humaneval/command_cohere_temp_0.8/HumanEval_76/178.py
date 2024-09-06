```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

The function checks whether the number `x` is a simple power of `n` by comparing it with `n ** int(x == n ** x)`. 

It returns `True` if `x` is a simple power of `n` and `False` otherwise. 

This solution works for positive integers only. Feel free to add your test cases to verify the functionality of the solution.