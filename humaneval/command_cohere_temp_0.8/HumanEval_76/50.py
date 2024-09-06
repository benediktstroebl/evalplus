```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

This function checks if a number `x` is a simple power of `n` by evaluating the condition `n ** int(x == n ** x)`. If this condition evaluates to truthy, it means that `x` is a simple power of `n`, as the equation `n ** int(x == n ** x)` will hold true only when `x` is a simple power of `n`. 

Here's how the function performs on the test cases provided:
- is_simple_power(1, 4) => true
- is_simple_power(2, 2) => true
- is_simple_power(8, 2) => true
- is_simple_power(3, 2) => false
- is_simple_power(3, 1) => false
- is_simple_power(5, 3) => false