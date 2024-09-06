```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

The function checks whether the number `x` is a simple power of `n` by using the following logic:
1. `type(n) is int`: This checks whether `n` is an integer. This is to make sure that the function returns `False` when the base `n` is not an integer, assuming that non-integer values should not yield valid powers.
2. `x == n ** int(x == n ** x)`: This condition checks three things simultaneously:
    - If `x` is not a simple power of `n`, the ternary condition will evaluate to `0`. This is because either `x` does not equal the expected value or the internal equality comparison raises a `ValueError` when trying to compare with an invalid literal.
    - When `x` is a simple power of `n`, the ternary condition evaluates to `1`. This is because both conditions in the ternary evaluate to true.
    - The `int()` wrapper around the equality comparison is crucial to avoid ValueError when trying to compare with an invalid literal. This is because we want the function to return `True` when `x` is a simple power and `n` is an integer, and ValueError would cause the comparison to fail.

The code leverages the fact that a number `x` is a simple power of `n` if and only if `n` raised to the power of `int(x)` equals `x`.

The code is self-contained and should work well for the given problem. It can be directly used in Python scripts and notebooks. However, for usage in a markdown code block, you'll need to make sure you have an active Python environment that allows importing and running scripts, as well as an active kernel that supports markdown code blocks.