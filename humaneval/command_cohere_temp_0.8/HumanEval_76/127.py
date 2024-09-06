```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

The function checks whether the number `x` is a simple power of `n` by using the following logic:
1. `type(n) is int`: This checks whether `n` is an integer. This is ensured to be true during the problem statement's examples.
2. `x == n ** int(x == n ** x)`: This condition checks three things simultaneously:
    - If `x` is a simple power of `n`. This is ensured by comparing `x` to `n` raised to the power of the integer `x`. This is the main condition to be satisfied.
    - If `x` is equal to `n` raised to the power of `x`. This is ensured by the equality check within the integer coercion.
    - If `x` is equal to `n` raised to the power of `int(x)`. This is ensured by the equality check within the integer coercion.

This solution leverages the fact that the `**` operator promotes its arguments to integers when applicable. Hence, it is correctly inferred that a simple power is exclusively an integer.

The code is fully self-contained as it does not rely on any external libraries or functions. It uses only standard Python features, making it readily executable on any platform that supports Python.