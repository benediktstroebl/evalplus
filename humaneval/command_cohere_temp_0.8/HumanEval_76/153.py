```python
def is_simple_power(x, n):
    return type(x) is int and x == n ** int(n ** 0.5)
```

This function examines the input number `x` and the base number `n`. It first checks whether `x` is an integer with the `type(x) is int` condition. If `x` is not an integer, the function returns false, as the product of any non-integer base and an exponent will always result in a non-integer value. Then, it checks if `x` equals `n` raised to the power of the integer portion of the square root of `n` (`n ** int(n ** 0.5)`). If all conditions are met, it returns true, indicating that `x` is a simple power of `n`. 

This approach efficiently determines whether `x` is a simple power of `n` while avoiding the need for additional imports or computations.