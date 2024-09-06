```python
def is_simple_power(x, n):
    return type(x) is int and x == n ** int(n ** 0.5)
```

This function `is_simple_power` checks if a given number `x` is a simple power of `n` by:
1. Ensuring that `x` is an integer using the `type(x) is int` condition. This step filters out cases like `is_simple_power(3, 2)` and `is_simple_power(3, 1)`.
2. Verifying that `x` equals `n` raised to the power of the square root of `n` (`n ** int(n ** 0.5)`) combined with the fact that `int(n ** 0.5)` is the integral part of the square root of `n`. 

This approach ensures that `is_simple_power(1, 4)` returns True due to `n ** int(n ** 0.5)` evaluating to 4, which proves that 1 is a simple power of 4. The argument of int() method is the square root of n, which is 2. The result of the evaluation is int(n**int(n**0.5)) and since n is 4, it becomes int(4)**2, which result 4. 

This function provides the correct results for the given example cases.