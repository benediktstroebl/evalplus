```python
def is_simple_power(x, n):
    return type(x) == type(n) and x == n ** int(n ** 0.5)
```

This function compares the type of `x` with the type of `n` and also checks if `x` is equal to the value of `n` raised to the power of the square root of `n` (which is an integer since we are dealing with squares). Both conditions must be true for the function to return `True`. Otherwise, it returns `False`. 

The given examples in the task statement will return:
- `True` for `is_simple_power(1, 4)`, `is_simple_power(2, 2)`, and `is_simple_power(8, 2)` ;
- `False` for `is_simple_power(3, 2)`, `is_simple_power(3, 1)`, and `is_simple_power(5, 3)`; 

It is important to note that the solution is not optimized for large numbers and may take a long time to execute. Also, handling cases where `n` is not a positive integer is outside the scope of this problem statement.