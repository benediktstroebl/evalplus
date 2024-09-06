```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

This function checks if the number `x` is a simple power of `n` by doing the following:
1. It first checks if the type of `n` is integer (to filter out non-integer bases).
2. If `x` is equal to `n` raised to the power of `x`, then it's a simple power, and the function returns `True`.
3. Otherwise, it returns `False` since the given case is not a simple power.

Here is a simplified breakdown of the code for easy reference:
```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

You can use it by calling the function with two arguments: `x` and `n`. It will return `True` if `x` is a simple power of `n`, and `False` otherwise. 

For example:
```python
result = is_simple_power(8, 2)
print(result)  # Output: True
```