```python
def is_simple_power(x, n):
    return type(x) == type(n)**int(n)**(x == n**int(n))
```
This function compares the type of `x` with the type of `n` raised to the power of `x`, returns `True` if they are the same, and `False` otherwise. The condition `x == n**int(n)` checks if `x` is a simple power of `n` since if `x` is a simple power then `n**int(n)` will give the same result as `x` and if `x` is not a simple power then the result of `n**int(n)` and `x` will not match. Note that this assumes that floating point numbers are not involved. The function is designed to work for positive integers, and updates would be needed for it to work in the general case.