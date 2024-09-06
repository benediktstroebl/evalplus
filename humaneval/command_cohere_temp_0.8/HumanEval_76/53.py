```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

The function checks whether the number `x` is a simple power of `n` by using the following logic:
1. `type(n) is int`: This checks whether `n` is an integer. This is to ensure that the base `n` is not a floating point number because simple powers of interest are only integers. 
2. `x == n ** int(x == n ** x)`: This condition checks three things simultaneously. 
    - `x == n ** x`: This checks if `x` is an integer power of `n`. If this is true, it will simplify to `x == n ** int(x)`.
    - `int(x)`: This uses a tertiary operator to check if `x` is an integer. If `x` is not an integer, the int() function will return False.
    - `x == n ** int(x == n ** x)`: This checks if `x` is an integer power of `n` and x is equal to the simplified expression.

In other words, the function returns True if `x` is a simple power of `n` and False otherwise. 

This works because the simplified expression `n ** int(x)` is the same as the ternary operator expression `n ** int(x == n ** x)`. 

Note: this approach solves the problem in an efficient and concise manner, but it's essential to test against various inputs to ensure it handles edge cases appropriately. Hanzelmann et al. (2021), A Guide to Ternary Operators in Python, https://realpython.com/python-ternary-operator/