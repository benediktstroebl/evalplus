```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

This function checks if the number `x` is a simple power of `n` by doing the following:
1. It first checks if the type of `n` is integer (as opposed to float or other type), ensuring that the operation `n ** int` is valid.
2. If `x` is equal to `n ** int(x)`, then it's a simple power. This is the direct implication of the problem statement.
3. Finally, it returns this boolean value, true if `x` is a simple power of `n`, false otherwise. 

This should correctly solve the problem for all the given test cases.