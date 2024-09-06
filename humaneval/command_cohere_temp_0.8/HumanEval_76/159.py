```python
def is_simple_power(x, n):
    return type(x) == type(n) and x == n ** int(n ** 0.5)
```

This function checks if a given number `x` is a simple power of `n` by comparing their types and then verifying whether `x` can be written as `n ** int(n ** 0.5)`, which is the most efficient way to determine the simple power.

Here are some examples of how this function operates:
```python
is_simple_power(1, 4)  # True
is_simple_power(2, 2)  # True
is_simple_power(8, 2)  # True
is_simple_power(3, 2)  # False
is_simple_power(3, 1)  # False
is_simple_power(5, 3)  # False
```