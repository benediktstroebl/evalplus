```python
def max_element(lst):
    return max(lst)

# Basic tests
print("max_element([1, 2, 3]) =", max_element([1, 2, 3]))
print("max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) =", max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))

# Edge case: Empty list
print("max_element([]) =", max_element([]))

# Edge case: Single element list
print("max_element([5]) =", max_element([5]))
```

This Python script defines a function `max_element(lst)` that returns the maximum element from a given list. It is then tested with various input lists, showcasing the function's behavior and handling edge cases effectively.