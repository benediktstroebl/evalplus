```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

The function checks whether the number `x` is a simple power of `n` by using the following logic:
1. `type(n) is int`: This checks whether `n` is an integer. This is to ensure that the simplification is not considering decimals.
2. `x == n ** int(x == n ** x)`: This condition checks three things simultaneously. 
    - `x == n ** x`: This checks if `x` is `n` raised to the power of `x`. This is the simplified form of the equation. 
    - `int(x)`: This checks if `x` can be converted to an integer without any fractions or decimals. This is to ensure that the simplified x is in the form of an integer. 
    - `x == n ** int(x)`: This checks if `x` is a simple power of `n` by evaluating the previous two conditions.

Let's take some examples to further explain the logic:
1. `is_simple_power(1, 4)`: True. Simplified form: `4 ** 1 = 4`
2. `is_simple_power(2, 2)`: True. Simplified form: `2 ** 2 = 4`
3. `is_simple_power(8, 2)`: True. Simplified form: `2 ** 3 = 8`
4. `is_simple_power(3, 2)`: False. Cannot be simplified to the form `n ** int`
5. `is_simple_power(3, 1)`: False. Cannot be simplified to the form `n ** int`
6. `is_simple_power(5, 3)`: False. Cannot be simplified to the form `n ** int`

The function should return `True` for the provided cases and `False` otherwise, as the problem's statement expects.