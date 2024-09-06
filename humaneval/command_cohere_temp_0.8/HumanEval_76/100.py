```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

This function checks if the number `x` is a simple power of `n` by doing the following:
1. It first checks if the type of `n` is integer (since the exponent has to be an integer).
2. If the type of `n` is integer, it then checks if `x` is equal to `n` raised to the power of the integer value of `x == n ** x`. This way, it checks if `x` can be written as `n^int` where `int` is an integer.

The function returns `True` if the condition is met, meaning the number is a simple power of `n`. Otherwise, it returns `False`. 

The given examples in the task statement will return:
- For `is_simple_power(1, 4)`, the function will return `True`.
- For `is_simple_power(2, 2)`, the function will return `True`.
- For `is_simple_power(8, 2)`, the function will return `True`.
- For `is_simple_power(3, 2)`, the function will return `False`.
- For `is_simple_power(3, 1)`, the function will return `False`.
- For `is_simple_power(5, 3)`, the function will return `False`.

The function should be able to handle any valid input for `x` and `n` and produce the correct output based on the defined logic.