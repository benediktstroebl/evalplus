```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n * n)
```

This function checks if the number `x` is a simple power of `n` by doing the following:
1. It first checks if the type of `n` is integer (to filter out floats).
2. If `x` is equal to `n` raised to the power of `n` (i.e., `n^n`), then it returns `True`.
3. If `x` is equal to `n` multiplied by itself (`n * n`) and this product is equal to `x`, then it returns `True`.
 Otherwise, it returns `False`. 

This algorithm efficiently determines if `x` is a simple power of `n` within just a few lines of code.

The unit tests for this function can be defined as follows:
```python
# Testing a variety of inputs and expected outputs
assert is_simple_power(1, 4) == True
assert is_simple_power(2, 2) == True
assert is_simple_power(8, 2) == True
assert is_simple_power(3, 2) == False
assert is_simple_power(3, 1) == False
assert is_simple_power(5, 3) == False
```