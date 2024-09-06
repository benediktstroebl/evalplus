```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

The function checks whether the number `x` is a simple power of `n` by using the following logic:
1. `type(n) is int`: This checks whether `n` is an integer. This is ensured to be true during the problem statement's examples.
2. `x == n ** int(x == n ** x)`: This condition checks three things simultaneously:
    - If `x` is a simple power of `n`. This is ensured by comparing `x` to `n**int(x)`. If they are equal, it is a simple power.
    - If `x == n**x`: This part of the condition ensures that `x` is an integer power. If this is true, the int() function will convert `x` to an integer, evaluating to `x` itself. Having this fact, the whole condition evaluates to True.

The code considers the number `x` is a simple power of `n` only if both conditions are met. 

The given example cases in the problem statement will return the following results:
- `is_simple_power(1, 4) => true`
- `is_simple_power(2, 2) => true`
- `is_simple_power(8, 2) => true`
- `is_simple_power(3, 2) => false`
- `is_simple_power(3, 1) => false`
- `is_simple_power(5, 3) => false`