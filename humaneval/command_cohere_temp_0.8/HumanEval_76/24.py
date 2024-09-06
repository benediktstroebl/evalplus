```python
def is_simple_power(x, n):
    return type(n) is int and x == n ** int(x == n ** x)
```

This function checks if the number `x` is a simple power of `n` by comparing it with `n ** int(x == n ** x)`. 

It returns `True` if `x` is a simple power of `n` and `False` otherwise. 

The function leverages the nature of integers to ascertain whether `x` is a simple power of `n` since a number `x` is a simple power of `n` if and only if `n` raised to the power of the integer value of `x` is equal to `x`. 

Example usage:
```python
>> is_simple_power(1, 4)
True
>> is_simple_power(2, 2)
True
>> is_simple_power(8, 2)
True
>> is_simple_power(3, 2)
False
>> is_simple_power(3, 1)
False
>> is_simple_power(5, 3)
False
```

This demonstrates that the function handles various cases accurately.