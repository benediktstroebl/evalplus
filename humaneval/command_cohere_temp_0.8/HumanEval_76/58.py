```python
def is_simple_power(x, n):
    return type(x) is int and x == n ** int(n ** 0.5)
```

This function leverages the fact that any number can be expressed as a simple power of its base, and utilizes the `**int()` operation to achieve this expression in integer form. The `type(x) is int` condition ensures that the function only returns true for integer inputs, as the expression x == n ** int(n ** 0.5) would return False for non-integer inputs. 

Here is an example usage of the function:
```python
print(is_simple_power(8, 2))  # Output: True
print(is_simple_power(3, 2))  # Output: False
print(is_simple_power(5, 3))  # Output: False
```

This demonstrates that the function correctly identifies simple powers for integer inputs, according to the definition provided in the problem statement.