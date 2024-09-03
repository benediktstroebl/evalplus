```python
def any_int(x, y, z):
    return (x + y == z) and (type(x) == int) and (type(y) == int) and (type(z) == int)

# Examples:
print(any_int(5, 2, 7))  # Output: True
print(any_int(3, 2, 2))  # Output: False
print(any_int(3, -2, 1))  # Output: True
print(any_int(3.6, -2.2, 2))  # Output: False
```
This code defines a function `any_int` that checks if two other numbers are equal to the sum of the other, and if all three are integers. The function returns `True` if all requirements are met, and `False` otherwise.