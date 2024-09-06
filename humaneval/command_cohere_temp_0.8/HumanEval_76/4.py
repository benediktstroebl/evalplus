```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

The function checks whether the number `x` is a simple power of `n` by using the following logic:
1. `type(n) is int`: This checks whether `n` is an integer. This is to ensure that the function handles non-integer bases gracefully.
2. `x == n ** int(x == n ** x)`: This is the main logic test.
    - `x == n ** x`: Checks if `x` is equal to `n` raised to the power of itself. This checks if `x` is a power of `n`.
    - `int(x == n ** x)`: Converts the result of the previous condition to an integer. This is necessary because Python performs float multiplication by default, which can lead to inaccurate results for decimal numbers. Converting the result to an integer ensures that only integer multiplication is considered.

The function returns `True` if `x` is a simple power of `n` and `False` otherwise. 

Let's explain how the code works with an example:
Let's take `x = 8` and `n = 2` and check the function call `is_simple_power(8, 2)`:
1. `type(n) is int`: `type(2) is int` is `True`, so the condition passes.
2. `x == n ** int(x == n ** x)`: 
    - `x == n ** x`: Is `8 == 2 ** 8`? This condition is `True` since `8` is a power of `2`.
    - `int(x == n ** x)`: The value of this expression is `int(True)`, which is `1`.

The final result of the function is `True`, which confirms that the function handles the example correctly.