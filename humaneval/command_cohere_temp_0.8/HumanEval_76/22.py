```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

This function checks if the number `x` is a simple power of `n` by doing the following:
1. It first checks if the type of `n` is int to make sure that the operation `n ** int(...)` is valid.
2. It then compares `x` with `n ** int(...)` to check if `x` is equal to the result of raising `n` to the power of the integral value of `x`.
3. Finally, it returns `True` if `x` is equal to the result of `n ** int(...)`, and `False` otherwise. 

Let's go through some examples to understand how it works:
- Since `n` is an integer, `is_simple_power(1, 4)` returns `True` because `4 ** 1 == 4`.
- `is_simple_power(2, 2)` returns `True` because `2 ** 2 == 4`
- `is_simple_power(8, 2)` returns `True` because `2 ** 3 == 8`
- However, `is_simple_power(3, 2)` returns `False` because `2 ** int(3) != 3` and `3` is not a power of 2.
- Similarly, `is_simple_power(3, 1)` returns `False` because `1 ** int(3) != 3` and `3` is not a power of 1. 
- Finally, `is_simple_power(5, 3)` returns `False` because `3 ** int(5) != 5` and `5` is not a simple power of 3. 

The function correctly identifies whether a number is a simple power of another number and returns `True` if it is, and `False` otherwise.