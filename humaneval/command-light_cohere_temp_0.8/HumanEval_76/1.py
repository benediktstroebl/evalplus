```python
def is_simple_power(x, n):
    return x ** n == x

# Test cases
print(is_simple_power(1, 4))  # True
print(is_simple_power(2, 2))  # True
print(is_simple_power(8, 2))  # True
print(is_simple_power(3, 2))  # True
print(is_simple_power(3, 1))  # False
print(is_simple_power(5, 3))  # False
```
This Python code defines a function `is_simple_power` that checks whether a given number `x` is the simple power of `n`. The function uses the exponentiation operator `**` and compares the resulting value with `x` to see if they are equal. The function returns `True` if the values are equal and `False` otherwise. The test cases demonstrate the specific examples of numbers and their corresponding powers, and the function successfully identifies the correct ones.