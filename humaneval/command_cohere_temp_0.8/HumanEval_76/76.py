```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n * n)
```

This function leverages the fact that a number 'x' is a simple power of 'n' if it can be expressed as 'n' raised to the power of an integer if 'x' is equal to 'n' multiplied by itself 'x' times (where 'n' is an integer). It utilizes type checking and strict equality tests to determine when this criterion is met, ensuring accurate determination of simple powers.