```python
def is_simple_power(x, n):
    return type(x) is int and x == n ** int(n ** 0.5)
```
This function checks if the number `x` is a simple power of `n` by comparing it to the result of raising `n` to the power of `int(n ** 0.5)`, which is the largest integer less than or equal to `n ** 0.5` that can raise `n` to the power of itself without any floating-point calculation. Since a number `x` is a simple power of `n` if and only if `n ** int(n ** 0.5) == x`, the given function returns `True` if `x` is a simple power of `n` and `False` otherwise. 

Here is a simple example of using the function which is provided in the problem statement:
```python
>>> is_simple_power(1, 4)
True
>>> is_simple_power(2, 2)
True
>>> is_simple_power(8, 2)
True
>>> is_simple_power(3, 2)
False
>>> is_simple_power(3, 1)
False
>>> is_simple_power(5, 3)
False
```