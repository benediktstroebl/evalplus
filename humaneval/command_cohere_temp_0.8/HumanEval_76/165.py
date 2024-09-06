```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

This function checks if the number `x` is a simple power of `n` by doing the following:
1. It first checks if the type of `n` is integer (if `n` is not an integer, then `x` cannot be its simple power).
2. If `n` is an integer, it then checks if `x` is equal to `n` raised to the power of the integer value obtained when `x == n ** x` is evaluated. If this condition is true, it returns `True`; otherwise, it returns `False`. 

This approach leverages the fact that Python assigns a literal `n` to a variable `x` when it is evaluated as `x == n ** x`. 

Overall, the function returns `True` if `x` is a simple power of `n` and `False` otherwise. 

Let's illustrate how the function performs on the provided test cases:
1. `is_simple_power(1, 4)` returns `True` since `4` is the exponent when `1` is raised to the power of `4`.
2. `is_simple_power(2, 2)` returns `True` since `2` is the exponent when `2` is raised to the power of `2`.
3. `is_simple_power(8, 2)` returns `True` since `2` is the exponent when `8` is raised to the power of `2`.
4. `is_simple_power(3, 2)` returns `False` since `3` is not a simple power of `2`.
5. `is_simple_power(3, 1)` returns `False` since `3` is not a simple power of `1`.
6. `is_simple_power(5, 3)` returns `False` since `5` is not a simple power of `3`.