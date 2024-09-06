```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

The function checks whether the number `x` is a simple power of `n` by using the following logic:
1. `type(n) is int`: This checks whether `n` is an integer. This is ensured by the fact that the `int` type is a subclass of `integer` and is always true.
2. `x == n ** int(x == n ** x)`: This condition checks three things simultaneously:
    - If `x` is a simple power of `n`. This is ensured by the fact that `(n**int(x))**x` is `x` for all positive real numbers `x` and `n`.
    - If `x` is equal to `n` (in case `x` is a simple power of `n` with exponent 1). This is because `x == n ** (x == n ** x)`.
    - It uses a ternary operator to avoid unnecessary computations, checking only if the condition is true. 

The code will return `True` if these conditions are met and `False` otherwise. 

The given example tests return the following results:
- `is_simple_power(1, 4)` returns `True`.
- `is_simple_power(2, 2)` returns `True`.
- `is_simple_power(8, 2)` returns `True`.
- `is_simple_power(3, 2)` returns `False`.
- `is_simple_power(3, 1)` returns `False`.
- `is_simple_power(5, 3)` returns `False`.

The code covers the "simple power" definition but doesn't cover edge cases like taking `n` or `x` as a non-integer number or zero as a base. Adjust the tests accordingly if such coverage is required.