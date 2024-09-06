```python
def is_simple_power(x, n):
    return type(x) is int and x == n ** int(n ** x == x)
```

This function evaluates to true when the argument `x` is an integer and equal to `n` raised to the power of the integer value of `n` that equals `x`. Otherwise, it returns false. 

**Example Usage:**
```python
> is_simple_power(1, 4)
True
> is_simple_power(2, 2)
True
> is_simple_power(8, 2)
True
> is_simple_power(3, 2)
False
> is_simple_power(3, 1)
False
> is_simple_power(5, 3)
False
```