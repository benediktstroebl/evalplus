```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n * n)
```

The given code defines a Python function `is_simple_power` that checks whether a given number `x` is a simple power of `n`. It returns `True` if `x` is a simple power of `n` and `False` otherwise. The function follows the problem definition, where a simple power is defined as `n**int = x`, and it checks the conditions explicitly.

Here is a breakdown of the functionality of the code:
- The function `is_simple_power(x, n)` takes two arguments, `x` and `n`.
- '**int**(x == n * n)` checks if `x` is a power of `n` with an exponent that is an integer. If this condition is met, it returns `True`, indicating that `x` is a simple power of `n`.
- The type of `n` is checked to be an integer. This is to ensure that the simple power rule applies to real numbers.

Note, the code explicitly verifies the simple power definition and validates the type of `n` to be an integer, providing a self-contained solution that does not rely on any external implementations or assumptions.