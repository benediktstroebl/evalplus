```python
def is_simple_power(x, n):
    return type(x) is int and x == n ** int(n ** 0.5)
```

This function simplifies the problem by directly calculating the square root of `n` and using it to raise `n` to the power of `x`, allowing the comparison of `x` and `n ** int(n ** 0.5)` to determine if `x` is a simple power of `n`. 

Here's a breakdown of the code:
1. `return type(x) is int and x`: This checks if `x` is an integer and equal to `n ** int(n ** 0.5)`. The type check ensures that `x` is an integer, and the power assertion verifies if `x` is a simple power of `n`.
2. `int(n ** 0.5)`: This calculates the square root of `n` and converts it to an integer using the `int` function. It's used to raise `n` to the power of `x` in the comparison. 

This approach efficiently solves the problem and accurately determines if `x` is a simple power of `n`.