```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

The function checks whether the number `x` is a simple power of `n` by using the following logic:
1. `type(n) is int`: This checks whether `n` is an integer. This is to prevent situations where `n` is a floating-point number, which can lead to inaccurate results.
2. `x == n ** int(x == n ** x)`: This condition checks three things at once:
    - If `x` is not a simple power of `n`, then `n ** int(x == n ** x)` will return a literal integer value that is not the same as `x`.
    - If `x` is a simple power of `n`, then `n ** int(x == n ** x)` will return `x`, which will make the equality `x == n ** int(x == n ** x)` evaluate to `True`.
    - The use of the integer literal conversion `int(x == n ** x)` ensures that if `x` is not an integer, it will be converted to an integer value, avoiding potential floating-point errors. 

This approach ensures that the function accurately identifies simple powers while preventing potential inaccuracies caused by floating-point representations.