```python
def is_simple_power(x, n):
    return type(x) is int and x == n ** int(n ** 0.5)
```

This function simplifies the problem by directly comparing the target number `x` with the `int` power of `n`, efficiently determining whether `x` is a simple power of `n`. 

The logic behind this approach involves utilizing the integer power property, which states that for positive integers `x` and `n`, if `x` is a positive integer power of `n`, then `x` equals `n` raised to the power of the integer value obtained from `x`. 

This property is inferred from the multiplication operation, where repeated addition of `n` to itself is simulated by multiplying `n` by itself multiple times. 

For instance, considering the value `x = 8` and the exponent `n = 2`:
8 = 2 * 2 * 2 
8 = 2 ** 3

Hence, the provided Python function efficiently solves the problem by directly comparing `x` with `n` raised to the power of its integer square root.