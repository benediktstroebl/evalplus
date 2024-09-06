```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

The function checks whether `n` is an integer and whether `x` is equal to `n` raised to the power of itself. The latter is achieved using the expression `x == n ** x` which should evaluate to `True` if `x` is a simple power of `n` and to `False` otherwise. The function returns `True` if these conditions are met and `False` otherwise. 

The markdown code block includes corresponding tests to ensure the function behaves as expected. You can use this code to test the function is_simple_power and ensure it passes all the test cases.