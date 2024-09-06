```python
def is_simple_power(x, n):
    return type(x) is int and x == n ** int(n ** 0.5)
```

This function examines the type of `x` to determine if it is an integer to verify if `x` is an integer and then checks if it equals `n` raised to the power of the square root of `n` to verify if it is a simple power of `n`. This is done in the return statement of the function. The function returns `true` if the input satisfies the given criterion and `false` otherwise.