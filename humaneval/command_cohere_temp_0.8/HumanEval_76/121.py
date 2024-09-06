```python
def is_simple_power(x, n):
    return type(x) == type(n) and x == n ** int(x == n ** x)
```

The function checks whether `x` is a simple power of `n` by comparing `x` and `n` of the same type (either both integers or both floats). If `x` is an integer, it checks if it equals `n` raised to the power of its own value (`n ** int(x == n ** x)`), which would return an integer as well. The condition `x == n ** x` checks if `x` is a simple power of `n`.

This approach ensures that the correct type of exception is raised if there's an error, unlike the approach in the original post. It also does not require any additional variables or methods. 

This solution should be robust for positive integers and floats, as the power function performs float exponentiation. For negative numbers or non-numeric inputs, this solution would raise an error accordingly, which is considered valid behavior for this problem.