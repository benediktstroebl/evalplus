```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

The function checks whether the number `x` is a simple power of `n` by using the following logic:
1. `type(n) is int`: This checks whether `n` is an integer. This is ensured to be true during the problem statement's examples.
2. `x == n ** int(x == n ** x)`: This condition checks three things simultaneously:
    - If `x` is a simple power of `n`. This is ensured by the equality `x == n ** int(x)`.
    - If `x` is equal to `n` raised to the power of the integer parts of `x` and `n`. This ensures that both `x` and `n` are powers of the same integer.
    - The use of the `int()` function ensures that the result of `x == n ** x` is cast to an integer, so the result of the equality checks if the floating point numbers match perfectly. 

The function returns `True` if these conditions hold, meaning that `x` is a simple power of `n`. Otherwise, it returns `False`.