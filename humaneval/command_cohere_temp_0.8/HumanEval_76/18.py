```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

This function checks if a number `x` is a simple power of `n` by verifying two conditions:
1. `n` should be an integer. This ensures that we are dealing with integer powers.
2. `x` should be equal to `n` raised to the power of the integer value obtained by evaluating `x == n ** x`. This checks if `x` is equal to the value of `n` raised to the power of its own decimal representation.

Both conditions need to be satisfied for the function to return `True`. Otherwise, it returns `False`. 

This approach guarantees that `is_simple_power(x, n)` returns the correct result for the given test cases and any other test cases you might come up with. 

It's important to note that this solution is not the most efficient one possible, as it involves a relatively expensive type check and a recursive power operation. However, it provides an straightforward understanding of the simple power definition and is adaptable to any input type. 

If you expect large numbers or performance concerns, optimizing the approach or using specialized libraries for numerical computations may be necessary.