```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

The function checks whether the number `x` is a simple power of `n` by using the following logic:
1. `type(n) is int`: This checks whether `n` is an integer. This is to ensure that the simplification is not performed for floats.
2. `x == n ** int(x == n ** x)`: This is the main part of the logic. 
    - `x == n ** x`: Checks if `x` can be written as `n` raised to the power of `x`. This is the simplified form of `x`.
    - `int(x == n ** x)`: This uses intuition to determine if the simplified form is an integer. We cast `x == n ** x` to an integer (`int(x == n ** x)`) and compare it to `x`. This step ensures that the simplified form is equal to the original number `x` and is an integer.

If the conditions are met, it returns `True`, indicating that `x` is a simple power of `n`. Otherwise, it returns `False`.

The code includes type checking to differentiate between integer and float simplification and determines whether the simplified form is an integer or not, which matches the markdown problem description.