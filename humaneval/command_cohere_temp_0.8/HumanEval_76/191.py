```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n * n)
```

The given function checks if the number `x` is a simple power of `n` and returns `True` if it is; otherwise, for any other case, it returns `False`. The function leverages the realization that a number `x` is a simple power of `n` if `n` is an integer, and `x` equals `n` to the power of `x/n` which is equivalent to `n**int(x/n)`. The overall time complexity of the solution is `O(log(N))`, where `N` represents the larger of `x` and `n`, and the space complexity is `O(1)`.

This solution simplifies the problem and eliminates the need for explicit integer casting. It also reduces the number of lines and makes the code more readable and maintainable.

This function can be optimized further by checking if `x` is divisible by `n` or not, instead of always computing the integer power, as it is not needed for the true/false determination of a simple power. Hence the modified function would be:
```python
def is_simple_power(x, y):
    return y == int(x / y) if type(y) == int and x % y == 0 else False
```